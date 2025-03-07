from SQLYExecutionError import SQLYExecutionError
from SQLYUtils import SQLYUtils


class BaseDBConnector:
    """
    A base class for database connectors that provides methods to execute SQL queries.

    Attributes:
        connection: A database connection object.

    Methods:
        execute_query(query: dict):
            Translates a query dictionary to SQL and executes it.

        _execute(sql, params):
            Executes a given SQL statement with parameters and handles the result.
    """
    def __init__(self, connection):
        """
        Initializes the BaseDBConnector with a database connection.

        Args:
            connection: The database connection object.
        """
        self.connection = connection

    def execute_query(self, query: dict):
        """
        Executes a SQL query constructed from the given dictionary.

        Args:
            query (dict): A dictionary representing the query to be executed.

        Returns:
            Any: The result of the executed query.
        """
        sql, params = SQLYUtils.translate_to_sql(query)
        return self._execute(sql, params)

    def _execute(self, sql, params):
        """
        Executes a given SQL statement with the provided parameters.

        Args:
            sql (str): The SQL statement to be executed.
            params (tuple or dict): The parameters to be used with the SQL statement.

        Returns:
            list: If the SQL statement is a SELECT query, returns the fetched results.
            str: If the SQL statement is not a SELECT query, returns a success message.

        Raises:
            SQLYExecutionError: If an error occurs during the execution of the SQL statement.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params)
            if sql.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            self.connection.commit()
            return "Query executed successfully"
        except Exception as e:
            raise SQLYExecutionError(f"{self.__class__.__name__} error: " + str(e)) from e
        finally:
            cursor.close()
