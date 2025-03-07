import MSSQLConnector
import MariaDBConnector
import OracleConnector
import PostgresConnector
from SQLYExecutionError import SQLYExecutionError
import SQLiteConnector


class DatabaseConnector:
    """
    DatabaseConnector is a utility class that provides a method to obtain a specific
    database connector instance based on the database type.

    Methods:
        get_connector(db_type: str, connection: Any) -> Any:
            Returns an instance of the appropriate database connector class based on
            the provided database type.

            Parameters:
                db_type (str): The type of the database (e.g., 'sqlite', 'mariadb', 'postgres', 'oracle', 'mssql').
                connection (Any): The connection object or connection string required to establish a connection to the database.

            Returns:
                An instance of the corresponding database connector class.

            Raises:
                SQLYExecutionError: If the provided database type is not supported.
    """
    @staticmethod
    def get_connector(db_type, connection):
        """
        Returns a database connector instance based on the specified database type.

        Args:
            db_type (str): The type of the database (e.g., "sqlite", "mariadb", "postgres", "oracle", "mssql").
            connection: The connection object or parameters required to establish the database connection.

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
            raise SQLYExecutionError("Unsupported database type: " + db_type)
        return connectors[db_type](connection)
