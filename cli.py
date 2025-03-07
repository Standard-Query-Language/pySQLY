import argparse
from SQLYExecutor import SQLYExecutor

def main():
    """
    Entry point for the SQLY CLI Tool.

    This function sets up the argument parser for the command-line interface,
    parses the provided arguments, and executes the SQLY query using the specified
    database type and connection details.

    Arguments:
    - query (str): SQLY query as a YAML string.
    - db_type (str): Database type (sqlite, mariadb, postgres, oracle, mssql).
    - datasource (str, optional): Database connection details.

    The function prints the result of the executed query.
    """
    parser = argparse.ArgumentParser(description="SQLY CLI Tool")
    parser.add_argument("query", type=str, help="SQLY query as a YAML string")
    parser.add_argument("--db_type", type=str, required=True, help="Database type (sqlite, mariadb, postgres, oracle, mssql)")
    parser.add_argument("--datasource", type=str, help="Database connection details")
    args = parser.parse_args()

    executor = SQLYExecutor(datasource=args.datasource, db_type=args.db_type)
    result = executor.execute(args.query)
    print(result)

if __name__ == "__main__":
    main()
