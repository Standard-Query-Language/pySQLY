"""Base implementation of the database connector interface."""

from typing import Any, Dict, List

from pysqly.core import SQLYUtils
from pysqly.errors import SQLYExecutionError

from .interface import IDBConnector


class BaseDBConnector(IDBConnector):
    """
    A base class for database connectors that provides methods to execute SQL queries.

    Attributes:
        connection: A database connection object.
    """

    def __init__(self, connection: Any) -> None:
        """
        Initialize the BaseDBConnector with a database connection.

        Args:
            connection: The database connection object.
        """
        self.connection = connection

    def execute_query(self, query: Dict[str, Any]) -> Any:
        """
        Execute a SQL query constructed from the given dictionary.

        Args:
            query: A dictionary representing the query to be executed.

        Returns:
            The result of the executed query.
        """
        sql, params = SQLYUtils.translate_to_sql(query)
        return self.execute(sql, params)

    def execute(self, sql: str, params: List[Any]) -> Any:
        """
        Execute a given SQL statement with the provided parameters.

        Args:
            sql: The SQL statement to be executed.
            params: The parameters to be used with the SQL statement.

        Returns:
            If the SQL statement is a SELECT query, returns the fetched results.
            If the SQL statement is not a SELECT query, returns a success message.

        Raises:
            SQLYExecutionError: If an error occurs during the execution of
            the SQL statement.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params)
            if sql.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            self.connection.commit()
            return "Query executed successfully"
        except Exception as e:
            raise SQLYExecutionError(
                f"{self.__class__.__name__} error: {str(e)}"
            ) from e
        finally:
            cursor.close()
