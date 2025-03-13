"""Microsoft SQL Server connector implementation."""

from typing import Any, Union

import pyodbc

from .base import BaseDBConnector


class MSSQLConnector(BaseDBConnector):
    """
    MSSQLConnector is a class that inherits from BaseDBConnector.

    This class provides a connection interface to Microsoft SQL Server databases.
    """

    def __init__(self, connection: Union[str, Any]) -> None:
        """
        Initialize the MSSQLConnector with a database connection.

        Args:
            connection: Either a connection string or a
                pyodbc Connection object. If a string is provided, it will be used to
                establish a new connection.

        Notes:
            If a connection string is provided, it should be in the format required by pyodbc,
            typically including server, database, authentication details, and other relevant parameters.
        """
        if isinstance(connection, str):
            connection = pyodbc.connect(connection)
        super().__init__(connection)
