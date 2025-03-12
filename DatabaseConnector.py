from MSSQLConnector import MSSQLConnector
from MariaDBConnector import MariaDBConnector
from OracleConnector import OracleConnector
from PostgresConnector import PostgresConnector
from SQLYExecutionError import SQLYExecutionError
from SQLYUtils import SQLYUtils
from SQLiteConnector import SQLiteConnector


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

    def execute_query(self, query: dict, db_type: str, connection: Any):
        """
        Executes a SQLY query against a specified database.

        Args:
            query (dict): The query dictionary"
            db_type (str): The type of the database (e.g., "sqlite", "mariadb", "postgres", "oracle", "mssql").
            connection: The connection object or parameters required to establish the database connection.

        Returns:
            The result of the executed query.

        Raises:
            SQLYExecutionError: If the query is invalid or an error occurs during execution.
        """
        db_connector = DatabaseConnector.get_connector(db_type, connection)
        sql, params = SQLYUtils.translate_to_sql(query)
        return db_connector.execute(sql, params)
