"""MariaDB connector implementation."""

from typing import Any, Union

import mysql.connector

from .base import BaseDBConnector


class MariaDBConnector(BaseDBConnector):
    """
    MariaDBConnector is a class that inherits from BaseDBConnector.

    This class provides a connection interface to a MariaDB/MySQL database.
    """

    def __init__(self, connection: Union[str, Any]) -> None:
        """
        Initialize the MariaDBConnector.

        This constructor accepts either a connection string or an existing MySQL connection.

        Args:
            connection: If a string is provided, it's treated as a connection string and a new connection is established.
                If a connection object is provided, it's used directly.
        """
        if isinstance(connection, str):
            connection = mysql.connector.connect(connection)
        super().__init__(connection)
