"""
pySQLY - SQL with YAML

A Python library that enables developers to write database queries
using YAML syntax instead of traditional SQL.
"""

from .errors import SQLYError, SQLYExecutionError, SQLYParseError
from .connectors import (
    IDBConnector,
    BaseDBConnector,
    SQLiteConnector,
    MariaDBConnector,
    PostgresConnector,
    OracleConnector,
    MSSQLConnector,
    DatabaseConnector,
)
from .core import SQLYExecutor, SQLYParser, SQLYUtils

__all__ = [
    "SQLYParser", "SQLYExecutor", "SQLYError", "SQLYParseError", "SQLYExecutionError",
    "SQLYUtils", "BaseDBConnector", "IDBConnector", "DatabaseConnector",
    "SQLiteConnector", "MariaDBConnector", "PostgresConnector", "OracleConnector", "MSSQLConnector"
]

__version__ = "0.1.0"
