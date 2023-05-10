import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

DB_HOST = os.environ.get("POSTGRES_HOST")
DB_DB = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_PORT = os.environ.get("POSTGRES_PORT")
SECRET = os.environ.get("SECRET")
DEBUG_APP = os.environ.get("DEBUG")
