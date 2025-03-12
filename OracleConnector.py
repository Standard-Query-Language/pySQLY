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
        if isinstance(connection, str):
            connection = cx_Oracle.connect(connection)
        super().__init__(connection)
