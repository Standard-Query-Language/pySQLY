"""Tests for the SQLYExecutor module."""

import pytest

from pysqly import SQLYExecutionError, SQLYExecutor, SQLYParseError


def test_executor_init():
    """Test SQLYExecutor initialization."""
    # Basic initialization
    executor = SQLYExecutor("test.db", "sqlite")
    assert executor.datasource == "test.db"
    assert executor.db_type == "sqlite"
    assert executor.db_connector is not None

    # Initialize without db_type should not create a connector
    executor = SQLYExecutor("test.db")
    assert executor.datasource == "test.db"
    assert executor.db_type is None
    assert executor.db_connector is None


def test_executor_invalid_query(sqlite_connection, monkeypatch):
    """Test execution with invalid query."""
    # Create executor with test database
    executor = SQLYExecutor(sqlite_connection, "sqlite")

    # Test with missing required fields
    with pytest.raises(SQLYExecutionError):
        executor.execute(
            """
        select:
          - id
          - name
        # Missing 'from' field
        """
        )

    # Test with invalid YAML
    with pytest.raises(SQLYParseError):
        executor.execute(
            """
        select:
          - id
          name  # Missing hyphen
        from: users
        """
        )


def test_executor_missing_db_type():
    """Test execution without specifying database type."""
    executor = SQLYExecutor("test.db")

    with pytest.raises(SQLYExecutionError):
        executor.execute(
            """
        select:
          - id
        from: users
        """
        )


def test_executor_query(sqlite_connector, monkeypatch):
    """Test successful query execution."""
    # Mock the execute_query method to avoid actual database operation
    monkeypatch.setattr(
        sqlite_connector,
        "execute_query",
        lambda query: [("Alice", "alice@example.com"), ("Bob", "bob@example.com")],
    )

    # Create executor with mocked connector
    executor = SQLYExecutor(sqlite_connector.connection, "sqlite")

    # Execute a test query
    result = executor.execute(
        """
    select:
      - name
      - email
    from: users
    where:
      - field: active
        operator: "="
        value: 1
    """
    )

    # Check the result
    assert len(result) == 2
    assert result[0] == ("Alice", "alice@example.com")
    assert result[1] == ("Bob", "bob@example.com")
