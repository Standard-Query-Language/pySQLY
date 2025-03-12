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
        db_connector = DatabaseConnector.DatabaseConnector(db_type, datasource)
        return db_connector.execute_query(query, db_type, datasource)

    @staticmethod
    def translate_to_sql(query: dict) -> tuple[str, list]:
        """
        Translates a dictionary query representation into a SQL query and its parameters.
        The query dictionary should have the following structure:
        {
            "select": ["field1", "field2", ...],  # Optional, defaults to ["*"]
            "from": "table_name",                 # Required
            "where": [                            # Optional
                {"field": "field_name", "operator": "=", "value": value},
                ...
            ]
        }
        Args:
            query (dict): Dictionary representing a SQL query
        Returns:
            tuple[str, list]: A tuple containing:
                - str: The SQL query string with placeholders
                - list: The parameter values to be used with the query
        Example:
            >>> query = {
            ...     "select": ["id", "name"],
            ...     "from": "users",
            ...     "where": [
            ...         {"field": "age", "operator": ">", "value": 18},
            ...         {"field": "status", "operator": "=", "value": "active"}
            ...     ]
            ... }
            >>> translate_to_sql(query)
            ('SELECT id, name FROM users WHERE age > %s AND status = %s', [18, 'active'])
        """

        # Use a placeholder approach for the entire query structure
        sql_parts = ["SELECT"]
        params = []

        # Handle SELECT clause
        select_fields = query.get("select", ["*"])
        sql_parts.append(", ".join(select_fields))  # This should be validated separately

        # Handle FROM clause
        sql_parts.append("FROM")
        sql_parts.append(query["from"])  # This should be validated separately

        # Handle WHERE clause
        where_conditions = query.get("where", [])
        if where_conditions:
            sql_parts.append("WHERE")
            where_clauses = []
            for cond in where_conditions:
                where_clauses.append(f"{cond['field']} {cond['operator']} %s")
                params.append(cond['value'])
            sql_parts.append(" AND ".join(where_clauses))

        sql = " ".join(sql_parts)
        return sql, params
