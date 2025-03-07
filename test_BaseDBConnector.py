import unittest
from unittest.mock import Mock
from BaseDBConnector import BaseDBConnector

class TestBaseDBConnector(unittest.TestCase):
    """
    Unit tests for the BaseDBConnector class.

    TestBaseDBConnector is a test case for testing the initialization of the BaseDBConnector class.

    Methods:
        test_init: Tests the initialization of the BaseDBConnector class with a mock connection object.
    """
    def test_init(self):
        """
        Test the initialization of the BaseDBConnector class.

        This test creates a mock connection object and initializes the BaseDBConnector
        with it. It then asserts that the connection attribute of the connector is set
        correctly to the mock connection.

        Assertions:
            - The connection attribute of the BaseDBConnector instance should be equal
              to the mock connection object.
        """
        # Create a mock connection object
        mock_connection = Mock()

        # Initialize the BaseDBConnector with the mock connection
        connector = BaseDBConnector(mock_connection)

        # Assert that the connection attribute is set correctly
        self.assertEqual(connector.connection, mock_connection)

if __name__ == '__main__':
    unittest.main()
