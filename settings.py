from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")
PROJECT_NAME = "amity_lake_weather"
VERSION = "1.0.0"
API_PREFIX = ""
SECRET_KEY = config("SECRET_KEY", cast=Secret, default="applesauce")
POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)
