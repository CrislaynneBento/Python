from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

db = client['Flask'] 

new_user = {
    "username": "Cris",
    "password": "123"
}

db.users.insert_one(new_user)
