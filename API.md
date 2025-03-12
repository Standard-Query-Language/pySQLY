# pySQLY API Documentation

This document provides detailed information about the pySQLY API.

## Table of Contents

- [SQLYExecutor](#sqlyexecutor)
- [SQLYParser](#sqlyparser)
- [SQLYUtils](#sqlyutils)
- [Database Connectors](#database-connectors)
  - [IDBConnector](#idbconnector)
  - [BaseDBConnector](#basedbconnector)
  - [Specific Connectors](#specific-connectors)
- [Error Handling](#error-handling)

## SQLYExecutor

The central class for executing SQLY queries.

### Constructor

```python
SQLYExecutor(datasource, db_type=None)
```

**Parameters:**

- `datasource`: Connection string or path to the database
- `db_type`: Type of database ("sqlite", "mariadb", "postgres", "oracle", "mssql")

### SQLYExecutor Methods

#### execute

```python
execute(query: str) -> Any
```

Executes a SQLY query string.

**Parameters:**

- `query`: A SQLY query in YAML format

**Returns:**

- Results from the database query execution

**Raises:**

- `SQLYExecutionError`: If execution fails
- `SQLYParseError`: If the YAML cannot be parsed

**Example:**

```python
executor = SQLYExecutor("mydb.sqlite", "sqlite")
results = executor.execute("""
select:
  - name
  - age
from: users
where:
  - field: age
    operator: ">"
    value: 18
""")
```

## SQLYParser

Handles parsing of SQLY query strings into structured dictionaries.

### SQLYParser Methods

#### parse

```python
SQLYParser.parse(query: str) -> dict
```

**Parameters:**

- `query`: SQLY query string in YAML format

**Returns:**

- Dictionary representation of the YAML query

**Raises:**

- `SQLYParseError`: If the YAML cannot be parsed

## SQLYUtils

Utility functions for SQLY operations.

### SQLYUtils Methods

#### validate_query

```python
SQLYUtils.validate_query(query: dict) -> bool
```

Validates if a query dictionary has all required fields.

**Parameters:**

- `query`: Dictionary representation of a SQLY query

**Returns:**

- `True` if valid, `False` otherwise

#### translate_to_sql

```python
SQLYUtils.translate_to_sql(query: dict) -> tuple[str, list]
```

Converts a SQLY dictionary to a SQL query string and parameters.

**Parameters:**

- `query`: Dictionary representation of a SQLY query

**Returns:**

- Tuple with SQL query string and parameter list

## Database Connectors

### IDBConnector

Interface for all database connectors.

#### IDBConnector Methods

##### execute_sql

```python
execute(sql, params) -> Any
```

Abstract method that must be implemented by all connectors.

### BaseDBConnector

Base implementation of the IDBConnector interface.

#### BaseDBConnector Methods

##### execute_query

```python
execute_query(query: dict) -> Any
```

Executes a query dictionary against the database.

##### execute

```python
execute(sql, params) -> Any
```

Executes raw SQL with parameters.

### Specific Connectors

pySQLY includes the following database-specific connectors:

- `SQLiteConnector`: For SQLite databases
- `MariaDBConnector`: For MariaDB/MySQL databases
- `PostgresConnector`: For PostgreSQL databases
- `OracleConnector`: For Oracle databases
- `MSSQLConnector`: For Microsoft SQL Server databases

Each connector inherits from `BaseDBConnector` and may include database-specific optimizations.

## Error Handling

pySQLY defines a hierarchy of exception classes for error handling:

- `SQLYError`: Base exception class for all pySQLY errors
  - `SQLYParseError`: Raised when parsing a SQLY query fails
  - `SQLYExecutionError`: Raised when executing a query fails

**Example:**

```python
from pysqly import SQLYExecutor, SQLYParseError, SQLYExecutionError

try:
    executor = SQLYExecutor("mydb.sqlite", "sqlite")
    results = executor.execute(query)
except SQLYParseError as e:
    print(f"Error parsing query: {e}")
except SQLYExecutionError as e:
    print(f"Error executing query: {e}")
```

For more detailed examples, see the [Examples](./EXAMPLES.md) document.
