"""Logging utilities."""

import logging
import sys
from src.server.config import settings


def setup_logger(name: str) -> logging.Logger:
    """
    Setup logger with configured format and level.

    Args:
        name: Logger name

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(settings.LOG_LEVEL)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
