import sqlite3
from BaseDBConnector import BaseDBConnector

class SQLiteConnector(BaseDBConnector):
    """
    SQLiteConnector is a class that inherits from BaseDBConnector.

    This class is intended to provide a connection interface to an SQLite database.
    Currently, it does not implement any specific methods or properties, but serves
    as a placeholder for future enhancements and functionalities specific to SQLite.

    Attributes:
        None

    Methods:
        None
    """
    def __init__(self, connection):
        """
        Initialize the SQLiteConnector with a connection to an SQLite database.

        Parameters
        ----------
        connection : str or sqlite3.Connection
            Either a file path to an SQLite database or an existing sqlite3.Connection object.
            If a string is provided, a new connection to the database at that path is created.

        Notes
        -----
        This class inherits from a parent connector class and passes the connection
        to the parent's constructor.
        """
        if isinstance(connection, str):
            connection = sqlite3.connect(connection)
        super().__init__(connection)
