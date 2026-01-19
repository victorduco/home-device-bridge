"""FastMCP server entrypoint."""

import fastmcp
import uvicorn
from starlette.responses import JSONResponse

from .app import create_app


if __name__ == "__main__":
    mcp = create_app()
    mcp_app = mcp.http_app(
        path="/",
        transport="http",
        json_response=True,
        stateless_http=True,
    )

    async def root_status(_request) -> JSONResponse:
        tools = await mcp.get_tools()
        resources = await mcp.get_resources()
        prompts = await mcp.get_prompts()

        tool_map = {}
        for name, tool in tools.items():
            tool_map[name] = {
                "name": tool.name or name,
                "description": tool.description or "",
                "inputSchema": tool.parameters,
            }

        resource_list = []
        for resource in resources.values():
            resource_list.append(
                {
                    "name": resource.name or resource.uri,
                    "description": resource.description or "",
                    "uri": str(resource.uri),
                    "mimeType": str(resource.mime_type) if resource.mime_type else None,
                }
            )

        prompt_list = []
        for prompt in prompts.values():
            arguments = []
            for arg in prompt.arguments or []:
                arguments.append(
                    {
                        "name": arg.name,
                        "description": arg.description or "",
                        "required": arg.required,
                        "schema": arg.schema,
                    }
                )
            prompt_list.append(
                {
                    "name": prompt.name,
                    "description": prompt.description or "",
                    "arguments": arguments,
                }
            )

        payload = {
            "server": {
                "name": mcp.name,
                "version": fastmcp.__version__,
                "transport": "http",
            },
            "capabilities": {
                "tools": tool_map,
                "resources": resource_list,
                "prompts": prompt_list,
            },
        }
        def json_safe(value):
            if value is None or isinstance(value, (str, int, float, bool)):
                return value
            if isinstance(value, dict):
                return {str(k): json_safe(v) for k, v in value.items()}
            if isinstance(value, (list, tuple, set)):
                return [json_safe(item) for item in value]
            if hasattr(value, "model_dump"):
                return json_safe(value.model_dump())
            if callable(value):
                return getattr(value, "__name__", "callable")
            return str(value)

        return JSONResponse(json_safe(payload))

    async def app(scope, receive, send):
        if scope.get("type") == "http" and scope.get("path") == "/" and scope.get("method") == "GET":
            response = await root_status(None)
            await response(scope, receive, send)
            return
        await mcp_app(scope, receive, send)

    uvicorn.run(app, host="0.0.0.0", port=8000)
