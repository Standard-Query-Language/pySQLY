"""Oracle connector implementation."""

from typing import Any, Union

import cx_Oracle

from .base import BaseDBConnector


class OracleConnector(BaseDBConnector):
    """
    OracleConnector is a class that inherits from BaseDBConnector.

    This class provides a connection interface to an Oracle database.
    """

    def __init__(self, connection: Union[str, Any]) -> None:
        """
        Initialize the OracleConnector.

        This constructor initializes a connection to an Oracle database using cx_Oracle.

        Args:
            connection: Either a connection string in the format
                "username/password@host:port/service_name" or an already established
                cx_Oracle Connection object. If a string is provided, it will be used
                to create a new connection.

        Notes:
            The connection string format follows the Oracle standard:
            "username/password@host:port/service_name"
        """
        if isinstance(connection, str):
            connection = cx_Oracle.connect(connection)
        super().__init__(connection)
