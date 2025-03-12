"""Main executor module for SQLY queries."""

from pysqly.errors import SQLYExecutionError
from pysqly.connectors import DatabaseConnector
from .parser import SQLYParser
from .utils import SQLYUtils


class SQLYExecutor:
    """
    Execute SQLY queries against database connections.

    Attributes:
        datasource: The data source against which the queries will be executed.
        db_type: The type of the database (optional).
        db_connector: The database connector instance.

    Methods:
        execute(query: str):
            Parses and validates the given SQLY query, then executes it.
            Raises SQLYExecutionError if the query is invalid or execution fails.
    """
    def __init__(self, datasource, db_type=None):
        """
        Initialize the executor with the given datasource and optional database type.

        Args:
            datasource (str): The path or identifier for the data source.
            db_type (str, optional): The type of the database (e.g., 'sqlite', 'mysql').
                                     Defaults to None.
        """
        self.datasource = datasource
        self.db_type = db_type
        self.db_connector = DatabaseConnector(db_type, datasource) if db_type else None

    def execute(self, query: str):
        """
        Execute the given SQLY query string.

        Args:
            query (str): The SQLY query string to be executed.

        Returns:
            Any: The result of the executed query.

        Raises:
            SQLYExecutionError: If the query is invalid or execution fails.
        """
        try:
            parsed_query = SQLYParser.parse(query)
            if not SQLYUtils.validate_query(parsed_query):
                raise SQLYExecutionError("Invalid SQLY query structure: Missing required fields.")
            return self._run_query(parsed_query)
        except Exception as e:
            raise SQLYExecutionError(f"Failed to process SQLY query: {str(e)}") from e

    def _run_query(self, parsed_query: dict):
        """
        Execute a parsed SQL query using the provided datasource and database type.

        Args:
            parsed_query (dict): The parsed SQL query to be executed.

        Returns:
            Any: The result of the executed query.

        Raises:
            SQLYExecutionError: If there is an error during query execution.
        """
        try:
            if not self.db_connector:
                raise SQLYExecutionError("Database type not specified for the executor.")

            return self.db_connector.execute_query(parsed_query)
        except Exception as e:
            raise SQLYExecutionError(f"Query execution error: {str(e)}") from e
