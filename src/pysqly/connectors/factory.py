"""Factory for creating database connectors."""

from pysqly.errors import SQLYExecutionError
from .sqlite import SQLiteConnector
from .mariadb import MariaDBConnector
from .postgres import PostgresConnector
from .oracle import OracleConnector
from .mssql import MSSQLConnector


class DBConnectorFactory:
    """
    Factory class for creating database connectors based on database type.

    This class implements the Factory Pattern to create the appropriate
    database connector instance based on the database type.
    """

    @staticmethod
    def create_connector(db_type, connection):
        """
        Create and return a database connector instance based on the specified database type.

        Args:
            db_type (str): The type of the database (e.g., "sqlite", "mariadb",
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
