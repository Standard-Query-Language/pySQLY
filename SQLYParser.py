import yaml

from SQLYParseError import SQLYParseError


class SQLYParser:

    @staticmethod
    def parse(query: str) -> dict:
        """
        Parses a SQLY query string into a dictionary.

        Args:
            query (str): The SQLY query string to be parsed.

        Returns:
            dict: The parsed representation of the SQLY query.

        Raises:
            SQLYParseError: If the query contains invalid SQLY syntax.
        """
        try:
            return yaml.safe_load(query)
        except yaml.YAMLError as e:
            raise SQLYParseError("Invalid SQLY syntax: " + str(e)) from e
