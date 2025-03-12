import mysql.connector
from BaseDBConnector import BaseDBConnector

class MariaDBConnector(BaseDBConnector):
    """
    MariaDBConnector is a class that inherits from BaseDBConnector.

    This class is intended to provide a connection interface to a MariaDB database.
    Currently, it does not implement any additional functionality beyond what is provided by BaseDBConnector.

    Attributes:
        Inherits all attributes from BaseDBConnector.

    Methods:
        Inherits all methods from BaseDBConnector.
    """
    def __init__(self, connection):
        if isinstance(connection, str):
            connection = mysql.connector.connect(connection)
        super().__init__(connection)
