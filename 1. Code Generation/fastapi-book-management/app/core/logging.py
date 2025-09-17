"""
Logging configuration for the book management application.
"""

import logging
import sys
from typing import Dict, Any
from datetime import datetime

from ..core.config import get_settings

settings = get_settings()


class ColorFormatter(logging.Formatter):
    """Custom formatter with color codes for different log levels."""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    COLORS = {
        logging.DEBUG: grey,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno)
        formatter = logging.Formatter(
            f"{log_color}%(asctime)s - %(name)s - %(levelname)s - %(message)s{self.reset}"
        )
        return formatter.format(record)


def setup_logging() -> None:
    """Set up application logging configuration."""

    # Set log level based on debug setting
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO

    # Create logger
    logger = logging.getLogger("book_management")
    logger.setLevel(log_level)

    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # Set formatter
    if settings.DEBUG:
        console_handler.setFormatter(ColorFormatter())
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False


def get_logger(name: str = "book_management") -> logging.Logger:
    """Get a logger instance."""
    return logging.getLogger(name)


def log_api_request(method: str, path: str, user_id: int = None, **kwargs) -> None:
    """Log API request information."""
    logger = get_logger("api")

    log_data = {
        "method": method,
        "path": path,
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        **kwargs
    }

    logger.info(f"API Request: {log_data}")


def log_api_response(method: str, path: str, status_code: int,
                    processing_time: float = None, **kwargs) -> None:
    """Log API response information."""
    logger = get_logger("api")

    log_data = {
        "method": method,
        "path": path,
        "status_code": status_code,
        "processing_time": processing_time,
        "timestamp": datetime.utcnow().isoformat(),
        **kwargs
    }

    logger.info(f"API Response: {log_data}")


def log_database_operation(operation: str, table: str, success: bool,
                          error: str = None, **kwargs) -> None:
    """Log database operation information."""
    logger = get_logger("database")

    log_data = {
        "operation": operation,
        "table": table,
        "success": success,
        "error": error,
        "timestamp": datetime.utcnow().isoformat(),
        **kwargs
    }

    if success:
        logger.info(f"Database Operation: {log_data}")
    else:
        logger.error(f"Database Operation Failed: {log_data}")


def log_authentication_event(event_type: str, username: str, success: bool,
                            reason: str = None, **kwargs) -> None:
    """Log authentication events."""
    logger = get_logger("auth")

    log_data = {
        "event_type": event_type,
        "username": username,
        "success": success,
        "reason": reason,
        "timestamp": datetime.utcnow().isoformat(),
        **kwargs
    }

    if success:
        logger.info(f"Authentication Event: {log_data}")
    else:
        logger.warning(f"Authentication Failed: {log_data}")


# Initialize logging
setup_logging()