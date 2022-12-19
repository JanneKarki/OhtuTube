"""Sets database filename so that tests don't use the same database as the app."""
from os import environ
environ['DATABASE_FILENAME'] = 'test_database.sqlite'
