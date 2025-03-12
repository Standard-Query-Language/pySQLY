import pyodbc
from BaseDBConnector import BaseDBConnector


class MSSQLConnector(BaseDBConnector):
    """
    MSSQLConnector is a class that inherits from BaseDBConnector.

    This class is intended to provide a connection interface to Microsoft SQL Server databases.
    Currently, it does not implement any specific methods or attributes.

    Attributes:
        None

    Methods:
        None
    """
    def __init__(self, connection):
        """
        Initializes the MSSQLConnector with a database connection.

        Args:
            connection (Union[str, pyodbc.Connection]): Either a connection string or a
                pyodbc Connection object. If a string is provided, it will be used to
                establish a new connection.

        Notes:
            If a connection string is provided, it should be in the format required by pyodbc,
            typically including server, database, authentication details, and other relevant parameters.
        """
        if isinstance(connection, str):
            connection = pyodbc.connect(connection)
        super().__init__(connection)
