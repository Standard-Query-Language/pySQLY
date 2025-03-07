import unittest
from SQLYParser import SQLYParser
from SQLYParseError import SQLYParseError

class TestSQLYParser(unittest.TestCase):
    """
    Test suite for the SQLYParser class.

    This test suite contains the following test cases:

    1. test_parse_valid_query:
        - Test case for parsing a valid SQLY query.
        - Verifies that the SQLYParser correctly parses a valid query string into the expected dictionary format.
        - The query string contains key-value pairs separated by colons and new lines.
        - Assertions: The parsed result from SQLYParser.parse(query) should match the expected_result dictionary.

    2. test_parse_invalid_query:
        - Test case for parsing an invalid SQLY query.
        - Verifies that the SQLYParser raises an SQLYParseError when attempting to parse a query with invalid syntax.
        - The query provided has a missing colon between 'key2' and 'value2', which should trigger the error.

    3. test_parse_empty_query:
        - Test case for parsing an empty SQL query.
        - Verifies that the SQLYParser correctly handles an empty query string by returning None.
        - Steps:
            1. Define an empty query string.
            2. Define the expected result as None.
            3. Parse the empty query string using SQLYParser.
            4. Assert that the result matches the expected result (None).

    Classes:
        TestSQLYParser: Contains unit tests for the SQLYParser class.

    Methods:
        test_parse_valid_query: Test case for parsing a valid SQLY query.
        test_parse_invalid_query: Test case for parsing an invalid SQLY query.
        test_parse_empty_query: Test case for parsing an empty SQL query.
    """
    def test_parse_valid_query(self):
        """
        Test case for parsing a valid SQLY query.

        This test verifies that the SQLYParser correctly parses a valid query string
        into the expected dictionary format.

        The query string contains key-value pairs separated by colons and new lines.
        The expected result is a dictionary with the corresponding key-value pairs.

        Assertions:
            The parsed result from SQLYParser.parse(query) should match the expected_result dictionary.
        """
        query = """
        key1: value1
        key2: value2
        """
        expected_result = {
            'key1': 'value1',
            'key2': 'value2'
        }
        result = SQLYParser.parse(query)
        self.assertEqual(result, expected_result)

    def test_parse_invalid_query(self):
        """
        Test case for parsing an invalid SQLY query.

        This test verifies that the SQLYParser raises an SQLYParseError
        when attempting to parse a query with invalid syntax. The query
        provided has a missing colon between 'key2' and 'value2', which
        should trigger the error.
        """
        query = """
        key1: value1
        key2 value2
        """
        with self.assertRaises(SQLYParseError):
            SQLYParser.parse(query)

    def test_parse_empty_query(self):
        """
        Test case for parsing an empty SQL query.

        This test verifies that the SQLYParser correctly handles an empty query string
        by returning None.

        Steps:
        1. Define an empty query string.
        2. Define the expected result as None.
        3. Parse the empty query string using SQLYParser.
        4. Assert that the result matches the expected result (None).
        """
        query = ""
        expected_result = None
        result = SQLYParser.parse(query)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
