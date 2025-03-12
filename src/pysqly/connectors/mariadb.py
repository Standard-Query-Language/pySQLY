"""MariaDB connector implementation."""

import mysql.connector
from .base import BaseDBConnector


class MariaDBConnector(BaseDBConnector):
    """
    MariaDBConnector is a class that inherits from BaseDBConnector.

    This class provides a connection interface to a MariaDB/MySQL database.
    """
    def __init__(self, connection):
        """
        Initialize the MariaDBConnector.

        This constructor accepts either a connection string or an existing MySQL connection.

        Parameters:
        ----------
        connection : str or mysql.connector.connection.MySQLConnection
            If a string is provided, it's treated as a connection string and a new connection is established.
            If a connection object is provided, it's used directly.
        """
        if isinstance(connection, str):
            connection = mysql.connector.connect(connection)
        super().__init__(connection)
