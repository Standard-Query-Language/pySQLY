# pySQLY - SQL with YAML

[![Python package](https://github.com/Standard-Query-Language/pySQLY/actions/workflows/python-package.yml/badge.svg)](https://github.com/Standard-Query-Language/pySQLY/actions/workflows/python-package.yml)
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

To include support for specific databases, use the optional extras:

```bash
# For MariaDB/MySQL support
pip install "pysqly[mariadb]"

# For PostgreSQL support
pip install "pysqly[postgres]"

# For Oracle support
pip install "pysqly[oracle]"

# For Microsoft SQL Server support
pip install "pysqly[mssql]"

# For all database support
pip install "pysqly[all]"
```

### Dependencies

pySQLY core requires only PyYAML. Additional database drivers are installed based on your needs:

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
- [Code of Conduct](./CODE_OF_CONDUCT.md) - Our community standards
- [Security Policy](./SECURITY.md) - Reporting vulnerabilities and security practices
- [Design Document](./DESIGN.md) - Architecture and design patterns
- [Changelog](./CHANGELOG.md) - Version history and changes

## Project Structure

```
pySQLY/
├── src/
│   └── pysqly/               # Main package directory
│       ├── __init__.py       # Package exports and version
│       ├── cli.py            # Command-line interface
│       ├── core/             # Core functionality
│       │   ├── __init__.py
│       │   ├── executor.py   # Main SQLY executor
│       │   ├── parser.py     # YAML to SQL parser
│       │   └── utils.py      # Helper utilities
│       ├── errors/           # Error handling
│       │   ├── __init__.py
│       │   ├── base.py       # Base error class
│       │   ├── execution.py  # Execution errors
│       │   └── parse.py      # Parsing errors
│       └── connectors/       # Database connectors
│           ├── __init__.py
│           ├── interface.py  # Connector interface
│           ├── base.py       # Base connector implementation
│           ├── factory.py    # Connector factory
│           ├── database.py   # Database connection manager
│           ├── sqlite.py     # SQLite connector
│           ├── mariadb.py    # MariaDB connector
│           ├── postgres.py   # PostgreSQL connector
│           ├── oracle.py     # Oracle connector
│           └── mssql.py      # MS SQL Server connector
├── tests/                    # Test directory
│   ├── __init__.py
│   ├── conftest.py           # Test fixtures and configuration
│   ├── test_parser.py        # Parser tests
│   └── test_utils.py         # Utilities tests
├── pyproject.toml            # Project metadata and dependencies
├── setup.py                  # Setup script (for backwards compatibility)
├── requirements.txt          # Development dependencies
├── MANIFEST.in               # Package manifest
├── LICENSE                   # MIT license
├── README.md                 # This file
├── API.md                    # API documentation
├── EXAMPLES.md               # Usage examples
├── CONTRIBUTING.md           # Contribution guidelines
├── CODE_OF_CONDUCT.md        # Code of conduct
├── SECURITY.md               # Security policy
├── DESIGN.md                 # Architecture design
└── CHANGELOG.md              # Version history
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

## Why Choose pySQLY?

- **Simplified Database Access**: Write database queries in a more readable format
- **Database Agnostic**: Switch between database systems without changing your query syntax
- **Reduced SQL Injection Risk**: Parameter binding is handled automatically
- **Improved Productivity**: Less boilerplate code and more intuitive query structure
- **Easy Integration**: Works with your existing Python applications

## License

pySQLY is distributed under the [MIT License](LICENSE).
