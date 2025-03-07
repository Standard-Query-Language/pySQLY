from SQLYParser import SQLYParser
from SQLYExecutionError import SQLYExecutionError
from SQLYUtils import SQLYUtils


class SQLYExecutor:
    """
    Executes SQLY queries against objects or databases.

    Attributes:
        datasource: The data source against which the queries will be executed.
        db_type: The type of the database (optional).

    Methods:
        execute(query: str):
            Parses and validates the given SQLY query, then executes it.
            Raises SQLYExecutionError if the query is invalid or execution fails.

        _run_query(parsed_query: dict):
            Executes the parsed SQLY query using the provided data source and database type.
            Raises SQLYExecutionError if the query execution fails.
    """
    def __init__(self, datasource, db_type=None):
        """
        Initializes the executer with the given datasource and optional database type.

        Args:
            datasource (str): The path or identifier for the data source.
            db_type (str, optional): The type of the database (e.g., 'sqlite', 'mysql'). Defaults to None.
        """
        self.datasource = datasource
        self.db_type = db_type

    def execute(self, query: str):
        """
        Executes the given SQLY query string.

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
            raise SQLYExecutionError("Failed to process SQLY query: " + str(e)) from e

    def _run_query(self, parsed_query: dict):
        """
        Executes a parsed SQL query using the provided datasource and database type.

        Args:
            parsed_query (dict): The parsed SQL query to be executed.

        Returns:
            Any: The result of the executed query.

        Raises:
            SQLYExecutionError: If there is an error during query execution.
        """
        try:
            return SQLYUtils.execute_query(parsed_query, self.datasource, self.db_type)
        except Exception as e:
            raise SQLYExecutionError("Query execution error: " + str(e)) from e
