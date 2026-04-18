from pymongo import MongoClient
import certifi

MONGO_URL = "mongodb+srv://tejaswinirajk_db_user:Rajagiri2323@cluster0.njjrtlw.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=30000)

db = client["cloud_db"]
collection = db["files"]