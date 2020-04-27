from os import environ
from redis import Redis
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = environ.get("TOKEN")
REDIS_CONN = {
    "host": "localhost",
    "port": 7777,
    "db": 5,
}
redis = Redis(
    **REDIS_CONN
)

# OUTPUT_RQ = Queue(connection=redis)
