import psycopg2
from BaseDBConnector import BaseDBConnector

class PostgresConnector(BaseDBConnector):
    """
    PostgresConnector is a class that inherits from BaseDBConnector and serves as a connector to a PostgreSQL database.

    Currently, this class does not implement any methods or properties, but it can be extended to include functionality
    specific to PostgreSQL database operations.

    Attributes:
        None

    Methods:
        None
    """
    def __init__(self, connection):
        if isinstance(connection, str):
            connection = psycopg2.connect(connection)
        super().__init__(connection)
