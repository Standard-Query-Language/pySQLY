import cx_Oracle
from BaseDBConnector import BaseDBConnector


class OracleConnector(BaseDBConnector):
    """
    OracleConnector is a class that inherits from BaseDBConnector.

    This class is intended to provide a connection interface to an Oracle database.
    Currently, it does not implement any specific functionality and serves as a placeholder
    for future methods and attributes specific to Oracle database connections.

    Attributes:
        None

    Methods:
        None
    """
    def __init__(self, connection):
        """
        Initialize the OracleConnector.

        This constructor initializes a connection to an Oracle database using cx_Oracle.

        Parameters
        ----------
        connection : str or cx_Oracle.Connection
            Either a connection string in the format "username/password@host:port/service_name"
            or an already established cx_Oracle Connection object.
            If a string is provided, it will be used to create a new connection.

        Notes
        -----
        The connection string format follows the Oracle standard:
        "username/password@host:port/service_name"

        Examples
        --------
        >>> # Using a connection string
        >>> connector = OracleConnector("user/pass@localhost:1521/XEPDB1")
        >>>
        >>> # Using an existing connection
        >>> conn = cx_Oracle.connect("user/pass@localhost:1521/XEPDB1")
        >>> connector = OracleConnector(conn)
        """
        if isinstance(connection, str):
            connection = cx_Oracle.connect(connection)
        super().__init__(connection)
