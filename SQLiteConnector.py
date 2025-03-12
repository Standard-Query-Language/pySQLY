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
        if isinstance(connection, str):
            connection = sqlite3.connect(connection)
        super().__init__(connection)
