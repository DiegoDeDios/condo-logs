from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


def get_db_manager(db_name):
    if(("DB_USER" not in os.environ) and ("DB_PWD") not in os.environ):
        raise Exception("Envrionment variables not set")
    db_user = os.getenv("DB_USER")
    db_pwd = os.getenv("DB_PWD")
    uri = f"mongodb+srv://{db_user}:{db_pwd}@cluster0.o5uv7co.mongodb.net/?retryWrites=true&w=majority"
    try:
        client = MongoClient(uri,server_api=ServerApi('1'))
        print("Connection successful")
        return client[db_name]
    except Exception as e:
        print(e)
        