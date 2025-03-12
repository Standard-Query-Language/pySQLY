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
        """
        Initialize the MariaDBConnector.

        This constructor accepts either a connection string or an existing MySQL connection.

        Parameters:
        ----------
        connection : str or mysql.connector.connection.MySQLConnection
            If a string is provided, it's treated as a connection string and a new connection is established.
            If a connection object is provided, it's used directly.

        Example:
        -------
            # Using a connection string
            connector = MariaDBConnector("host=localhost;user=root;password=secret;database=mydb")

            # Using an existing connection
            conn = mysql.connector.connect(host='localhost', user='root', password='secret')
            connector = MariaDBConnector(conn)
        """
        if isinstance(connection, str):
            connection = mysql.connector.connect(connection)
        super().__init__(connection)
