from SQLYError import SQLYError


class SQLYParseError(SQLYError):
    """
    Exception raised for errors in the parsing of a SQLY query.

    Attributes:
        message -- explanation of the error
    """
