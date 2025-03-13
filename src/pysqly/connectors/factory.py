"""Factory for creating database connectors."""

from typing import Any

from pysqly.errors import SQLYExecutionError

from .mariadb import MariaDBConnector
from .mssql import MSSQLConnector
from .oracle import OracleConnector
from .postgres import PostgresConnector
from .sqlite import SQLiteConnector


class DBConnectorFactory:
    """
    Factory class for creating database connectors based on database type.

    This class implements the Factory Pattern to create the appropriate
    database connector instance based on the database type.
    """

    @staticmethod
    def create_connector(db_type: str, connection: Any) -> Any:
        """
        Create and return a database connector instance based on the specified database type.

        Args:
            db_type: The type of the database (e.g., "sqlite", "mariadb",
                    "postgres", "oracle", "mssql").
            connection: The connection object or parameters required to establish
                    the database connection.

        Returns:
            An instance of the corresponding database connector class.

        Raises:
            SQLYExecutionError: If the specified database type is not supported.
        """
        connectors = {
            "sqlite": SQLiteConnector,
            "mariadb": MariaDBConnector,
            "postgres": PostgresConnector,
            "oracle": OracleConnector,
            "mssql": MSSQLConnector,
        }
        if db_type not in connectors:
            raise SQLYExecutionError(f"Unsupported database type: {db_type}")
        return connectors[db_type](connection)
