"""Utility functions for working with SQLY queries."""

from typing import Any, Dict, List, Tuple


class SQLYUtils:
    """
    Utility class providing static methods for validating and translating SQLY queries.

    Methods:
        validate_query(query: dict) -> bool:
            Checks if the provided query dictionary contains the necessary fields.

        translate_to_sql(query: dict) -> tuple[str, list]:
            Translates a dictionary query representation into a SQL query and parameters.
    """

    @staticmethod
    def validate_query(query: Any) -> bool:
        """
        Validate if the given query dictionary contains the necessary fields.

        Args:
            query: The query dictionary to validate.

        Returns:
            True if the query contains the "select" and "from" fields, False otherwise.
        """
        return isinstance(query, dict) and "select" in query and "from" in query

    @staticmethod
    def translate_to_sql(query: Dict[str, Any]) -> Tuple[str, List[Any]]:
        """
        Translate a dictionary query representation into a SQL query and its parameters.

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
            query: Dictionary representing a SQL query
        Returns:
            A tuple containing:
                - The SQL query string with placeholders
                - The parameter values to be used with the query
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
        params: List[Any] = []

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
                params.append(cond["value"])
            sql_parts.append(" AND ".join(where_clauses))

        sql = " ".join(sql_parts)
        return sql, params
