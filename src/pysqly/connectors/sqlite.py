"""SQLite connector implementation."""

import sqlite3
from .base import BaseDBConnector


class SQLiteConnector(BaseDBConnector):
    """
    SQLiteConnector is a class that inherits from BaseDBConnector.

    This class provides a connection interface to an SQLite database.
    """
    def __init__(self, connection):
        """
        Initialize the SQLiteConnector with a connection to an SQLite database.

        Parameters
        ----------
        connection : str or sqlite3.Connection
            Either a file path to an SQLite database or an existing sqlite3.Connection object.
            If a string is provided, a new connection to the database at that path is created.
        """
        if isinstance(connection, str):
            connection = sqlite3.connect(connection)
        super().__init__(connection)
