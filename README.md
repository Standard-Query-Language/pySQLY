# SQLY Python Module

## Overview

SQLY is a domain-specific query language designed to interact with various databases in a structured YAML format. This Python module provides an interface for integrating SQLY within applications, allowing developers to execute queries across multiple database systems seamlessly.

## Features

- Supports SQLite, MariaDB, PostgreSQL, Oracle, and MSSQL.
- YAML-based query syntax for simplicity and readability.
- Follows DRY, SOLID, and ACID principles for maintainability and reliability.
- CLI tool for quick command-line execution of SQLY queries.

## Installation

To install SQLY, run:

```sh
pip install pysqly
```

## Usage

### Using the Python API

```python
from sqly.executor import SQLYExecutor

datasource = "your_database_connection"
db_type = "postgres"  # Choose from sqlite, mariadb, postgres, oracle, mssql

executor = SQLYExecutor(datasource, db_type)
query = """
select:
  - name
  - age
from: users
where:
  - field: age
    operator: ">"
    value: 18
"""

result = executor.execute(query)
print(result)
```

### Using the CLI Tool

```sh
sqly-cli "select: [name, age]\nfrom: users\nwhere:\n  - field: age\n    operator: '>'\n    value: 18" --db_type postgres --datasource "your_db_connection"
```


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance SQLY.

## License

This project is licensed under the MIT License.
