import os
from pymongo import MongoClient

MONGO_URL = os.getenv("mongodb+srv://tejaswinirajk_db_user:Rajagiri2323@cluster0.njjrtlw.mongodb.net/cloud_db?retryWrites=true&w=majority")

client = MongoClient(MONGO_URL)
db = client["cloud_storage"]

files_collection = db["files"]
users_collection = db["users"]