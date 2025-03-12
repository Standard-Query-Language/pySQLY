"""Exception classes for pySQLY."""

from .base import SQLYError
from .parse import SQLYParseError
from .execution import SQLYExecutionError

__all__ = ["SQLYError", "SQLYParseError", "SQLYExecutionError"]
