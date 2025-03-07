from setuptools import setup, find_packages

setup(
    name="pySQLY",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pyyaml", "mysql-connector-python", "psycopg2", "cx_Oracle", "pyodbc"],
    entry_points={
        "console_scripts": [
            "sqly-cli=sqly.cli:main",
        ]
    },
)
