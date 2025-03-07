import DatabaseConnector


class SQLYUtils:
    """
    SQLYUtils is a utility class that provides static methods for validating and executing SQLY queries.

    Methods:
        validate_query(query: dict) -> bool:
            Checks if the provided query dictionary contains the necessary fields for a SQLY query.
            Args:
                query (dict): The query dictionary to validate.
            Returns:
                bool: True if the query contains the "select" and "from" fields, False otherwise.

        execute_query(query: dict, datasource, db_type):
            Executes a SQLY query against a specified database.
            Args:
                query (dict): The query dictionary to execute.
                datasource: The data source to connect to.
                db_type: The type of the database (e.g., MySQL, PostgreSQL).
            Returns:
                The result of the executed query.
    """
    @staticmethod
    def validate_query(query: dict) -> bool:
        """
        Validates if the given query dictionary contains the necessary fields.

        Args:
            query (dict): The query dictionary to validate.

        Returns:
            bool: True if the query contains the "select" and "from" fields, False otherwise.
        """
        return isinstance(query, dict) and "select" in query and "from" in query

    @staticmethod
    def execute_query(query: dict, datasource, db_type):
        """
        Executes a SQLY query against a database.

        Args:
            query (dict): The SQLY query to be executed.
            datasource: The data source to connect to.
            db_type: The type of the database (e.g., MySQL, PostgreSQL).

        Returns:
            The result of the executed query.
        """
        db_connector = DatabaseConnector.get_connector(db_type, datasource)
        return db_connector.execute_query(query)

    @staticmethod
    def translate_to_sql(query: dict):
        """Converts a SQLY query dictionary into SQL and parameters."""
        select_clause = ", ".join(query.get("select", ["*"]))
        from_clause = query["from"]
        where_conditions = query.get("where", [])
        where_clause = " AND ".join([f"{cond['field']} {cond['operator']} %s" for cond in where_conditions])
        params = [cond['value'] for cond in where_conditions]
        sql = f"SELECT {select_clause} FROM {from_clause}"
        if where_clause:
            sql += f" WHERE {where_clause}"
        return sql, params
