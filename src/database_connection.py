import os
import sqlite3
from config import DATABASE_FILE_PATH

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.isolation_level = None


def get_database_connection(test_db=None):
    if not test_db:
        return connection

    testdb_connection = sqlite3.connect(test_db)
    testdb_connection.isolation_level = None
    return testdb_connection
