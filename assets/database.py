from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:test1234@cluster0.yiog3b8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

asset_db = client.asset_db
metrics_db = client.metrics
users_db = client.users_db

asset_collection = asset_db["asset_db"]
metrics_collection = metrics_db["db.metrics_db"]
users_collection = users_db["users_db"]
