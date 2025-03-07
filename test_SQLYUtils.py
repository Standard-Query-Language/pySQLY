import unittest
from SQLYUtils import SQLYUtils

class TestSQLYUtils(unittest.TestCase):
    """
    Unit tests for the SQLYUtils class.

    Test Cases:
    - test_validate_query_valid: Tests that a valid query dictionary with 'select' and 'from' keys returns True.
    - test_validate_query_missing_select: Tests that a query dictionary missing the 'select' key returns False.
    - test_validate_query_missing_from: Tests that a query dictionary missing the 'from' key returns False.
    - test_validate_query_empty_dict: Tests that an empty query dictionary returns False.
    - test_validate_query_not_dict: Tests that a query which is not a dictionary returns False.
    """

    def test_validate_query_valid(self):
        """
        Test case for validating a correct SQL query structure.

        This test checks if the `validate_query` method of `SQLYUtils` correctly
        identifies a valid query structure. The query structure being tested
        includes a "select" key with a list of columns and a "from" key with the
        table name.

        The test asserts that the `validate_query` method returns True for the
        given valid query.
        """
        query = {
            "select": ["id", "name"],
            "from": "users"
        }
        self.assertTrue(SQLYUtils.validate_query(query))

    def test_validate_query_missing_select(self):
        """
        Test case for validating a query that is missing the 'select' clause.

        This test ensures that the `validate_query` method of the `SQLYUtils` class
        returns `False` when the query dictionary does not contain the required 'select' key.

        The query dictionary in this test case only contains the 'from' key with the value 'users'.
        """
        query = {
            "from": "users"
        }
        self.assertFalse(SQLYUtils.validate_query(query))

    def test_validate_query_missing_from(self):
        """
        Test case for the validate_query method in SQLYUtils class.

        This test checks the scenario where the 'from' clause is missing in the query.
        The query dictionary contains only the 'select' clause with fields 'id' and 'name'.
        The test asserts that the validate_query method should return False, indicating
        that the query is invalid due to the missing 'from' clause.
        """
        query = {
            "select": ["id", "name"]
        }
        self.assertFalse(SQLYUtils.validate_query(query))

    def test_validate_query_empty_dict(self):
        """
        Test case for SQLYUtils.validate_query method with an empty dictionary.

        This test verifies that the validate_query method returns False when
        an empty dictionary is passed as the query parameter.
        """
        query = {}
        self.assertFalse(SQLYUtils.validate_query(query))

    def test_validate_query_not_dict(self):
        """
        Test case for SQLYUtils.validate_query method.

        This test checks that the validate_query method returns False when the input query is not a dictionary.

        Assertions:
            - The method should return False when a string query is provided.
        """
        query = "SELECT * FROM users"
        self.assertFalse(SQLYUtils.validate_query(query))

if __name__ == '__main__':
    unittest.main()
