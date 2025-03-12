# pySQLY - SQL with YAML

[![Python package](https://github.com/yourusername/pySQLY/actions/workflows/python-package.yml/badge.svg)](https://github.com/yourusername/pySQLY/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/pysqly.svg)](https://badge.fury.io/py/pysqly)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

pySQLY is a Python library that enables developers to write database queries using YAML syntax instead of traditional SQL. This approach simplifies database interactions, enhances readability, and provides a consistent interface across multiple database systems.

### Key Features

- **Multi-Database Support**: Works with SQLite, MariaDB/MySQL, PostgreSQL, Oracle, and Microsoft SQL Server
- **YAML-Based Syntax**: Intuitive, structured query format that reduces syntax errors
- **Unified Interface**: Single API to interact with different database systems
- **CLI Support**: Run SQLY queries directly from the command line
- **Type Safety**: Leverages Python type annotations for better IDE support and error checking

## Installation

Install pySQLY from PyPI:

```bash
pip install pysqly
```

### Dependencies

pySQLY requires the following database drivers depending on which databases you intend to use:

- SQLite: Built into Python standard library
- MariaDB/MySQL: `mysql-connector-python`
- PostgreSQL: `psycopg2`
- Oracle: `cx_Oracle`
- Microsoft SQL Server: `pyodbc`

## Quick Start

### Basic Query Example

```python
from pysqly import SQLYExecutor

# Connect to a SQLite database
executor = SQLYExecutor("path/to/database.db", "sqlite")

# Define your query in YAML format
query = """
select:
  - username
  - email
  - created_at
from: users
where:
  - field: active
    operator: "="
    value: true
  - field: last_login
    operator: ">"
    value: "2023-01-01"
"""

# Execute the query
results = executor.execute(query)
print(results)
```

### Using the CLI

```bash
sqly-cli "select: [username, email]\nfrom: users\nwhere:\n  - field: active\n    operator: '='\n    value: true" --db_type sqlite --datasource "path/to/database.db"
```

## Documentation

- [API Documentation](./API.md) - Detailed library API reference
- [Examples](./EXAMPLES.md) - More usage examples and patterns
- [Contributing](./CONTRIBUTING.md) - Guidelines for contributing to pySQLY

## Project Structure

```bash
pySQLY/
├── __init__.py                 # Package exports
├── IDBConnector.py             # Database connector interface
├── BaseDBConnector.py          # Base implementation of the connector interface
├── SQLYParser.py               # YAML to SQL parser
├── SQLYExecutor.py             # Main query executor
├── SQLYUtils.py                # Helper utilities
├── DBConnectorFactory.py       # Factory for database connectors
└── database_connectors/        # Specific database implementations
    ├── SQLiteConnector.py
    ├── MariaDBConnector.py
    ├── PostgresConnector.py
    ├── OracleConnector.py
    └── MSSQLConnector.py
```

## SQLY Query Format

SQLY queries use YAML syntax to represent SQL operations:

```yaml
# Basic SELECT query
select:
  - column1
  - column2
from: table_name
where:
  - field: column1
    operator: "="
    value: some_value
```

See the [Examples](./EXAMPLES.md) document for more complex query patterns.

## License

pySQLY is distributed under the [MIT License](LICENSE).
