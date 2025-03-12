from DBConnectorFactory import DBConnectorFactory
from SQLYExecutionError import SQLYExecutionError


class DatabaseConnector:
    """
    DatabaseConnector is a utility class that provides methods to connect to
    and execute queries against different types of databases.
    """
    def __init__(self, db_type, connection):
        """
        Initializes the DatabaseConnector with the database type and connection information.

        Args:
            db_type (str): The type of the database (e.g., "sqlite", "mariadb", "postgres", "oracle", "mssql").
            connection: The connection object or parameters required to establish the database connection.
        """
        self.db_type = db_type
        self.connection = connection
        self.connector = None

    def _ensure_connector(self):
        """
        Ensures that a connector instance exists, creating it if necessary.

        Returns:
            The database connector instance.
        """
        if self.connector is None:
            self.connector = DBConnectorFactory.create_connector(self.db_type, self.connection)
        return self.connector

    def execute_query(self, query: dict, db_type=None, connection=None):
        """
        Executes a SQLY query against a specified database.

        Args:
            query (dict): The query dictionary"
            db_type (str, optional): The type of the database. Defaults to the instance's db_type.
            connection (optional): The connection object or parameters. Defaults to the instance's connection.

        Returns:
            The result of the executed query.

        Raises:
            SQLYExecutionError: If the query is invalid or an error occurs during execution.
        """
        # Use provided values or fall back to instance attributes
        db_type = db_type or self.db_type
        connection = connection or self.connection

        if db_type != self.db_type or connection != self.connection:
            # If parameters differ from instance attributes, create a new connector
            connector = DBConnectorFactory.create_connector(db_type, connection)
        else:
            connector = self._ensure_connector()

        # Execute the query using the appropriate connector
        return connector.execute_query(query)
