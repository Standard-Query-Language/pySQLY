import unittest
from SQLYExecutor import SQLYExecutor

class TestSQLYExecutor(unittest.TestCase):
    """
    Unit tests for the SQLYExecutor class.

    This test suite contains tests to verify the correct initialization of the
    SQLYExecutor class with different parameters.

    Classes:
        TestSQLYExecutor: Contains unit tests for the SQLYExecutor class.

    Methods:
        test_init_with_datasource_only: Tests the initialization of SQLYExecutor with only the datasource parameter.
        test_init_with_datasource_and_db_type: Tests the initialization of SQLYExecutor with a datasource and database type.
    """
    def test_init_with_datasource_only(self):
        """
        Test the initialization of SQLYExecutor with only the datasource parameter.

        This test verifies that the SQLYExecutor is correctly initialized when only
        the datasource parameter is provided. It checks that the datasource attribute
        is set correctly and the db_type attribute is None.

        Assertions:
            - The datasource attribute of the executor should match the provided datasource.
            - The db_type attribute of the executor should be None.
        """
        datasource = "path/to/datasource"
        executor = SQLYExecutor(datasource)
        self.assertEqual(executor.datasource, datasource)
        self.assertIsNone(executor.db_type)

    def test_init_with_datasource_and_db_type(self):
        """
        Test the initialization of SQLYExecutor with a datasource and database type.

        This test verifies that the SQLYExecutor object is correctly initialized
        with the provided datasource and database type. It checks that the
        datasource and db_type attributes of the executor match the expected values.

        Assertions:
            - The datasource attribute of the executor should match the provided datasource.
            - The db_type attribute of the executor should match the provided db_type.
        """
        datasource = "path/to/datasource"
        db_type = "sqlite"
        executor = SQLYExecutor(datasource, db_type)
        self.assertEqual(executor.datasource, datasource)
        self.assertEqual(executor.db_type, db_type)



if __name__ == '__main__':
    unittest.main()
