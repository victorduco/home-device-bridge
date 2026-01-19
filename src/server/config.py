"""Configuration and shared constants."""

import os

HA_URL = os.getenv("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.getenv("HA_TOKEN", "")

NOTIFICATION_GUIDE = """Home Assistant notification tool guide.

Tool name: send_notification
Required fields:
- device: Mobile app device slug (e.g. "iphone_13_pro")
- title: Short title (<= 60 chars)
- message: Main message (<= 240 chars)

Optional fields:
- subtitle: Secondary line, keep short
- sound: Push sound name (default: "default")
- data: Dict for extra mobile_app fields (e.g. {"priority": "high"})

Notes:
- The device maps to notify.mobile_app_<device> in Home Assistant.
- If you only have a device name, ask the user to confirm the slug.
- Prefer concise, action-oriented phrasing.

Example payload:
{
  "device": "iphone_13_pro",
  "title": "Door open",
  "message": "Front door opened 2 minutes ago.",
  "subtitle": "Security",
  "sound": "default",
  "data": {"priority": "high"}
}
"""
