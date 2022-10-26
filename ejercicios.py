from pymongo import MongoClient
import json


MONGO_HOST = "127.0.0.1:27017"
FILE_MOCK = "MOCK_DATA.json"
DATA = [
    {
        "first_name": "Manuel",
        "last_name": "Gomez",
        "email": "manogo@gmail.com",
        "gender": "Male",
        "ip_address": "15.208.64.26",
        "Latitude": 43.6342238,
        "Altitude": -3.41144,
        "City": "Madrid",
        "University": "UPSA"
    },
    {
        "first_name": "Lucia",
        "last_name": "Sanchez",
        "email": "lucisan@gmail.com",
        "gender": "Female",
        "ip_address": "5.208.64.76",
        "Latitude": 43.1342238,
        "Altitude": -2.41144,
        "City": "Salamanca",
        "University": "UPSA"
    },
    {
        "first_name": "Sergio",
        "last_name": "Suarez",
        "email": "sergiosua@gmail.com",
        "gender": "Male",
        "ip_address": "5.208.65.29",
        "Latitude": 43.1342238,
        "Altitude": -2.61144,
        "City": "Salamanca",
        "University": "UPSA"
    }]

def get_print_from_cursor(message, cursor):
    print(message)
    for item in cursor:
        print(item)

def import_json(database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    with open('MOCK_DATA.json', encoding='utf-8') as f:
        file_data = json.load(f)
        db.get_collection(collection).insert_many(file_data)
    client.close()

def insert_data(data, database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    db.get_collection(collection).insert_many(data)
    client.close()

def run_count(database, collection, query):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    client.close()
    results = db.get_collection(collection).count_documents(query)
    return results

def count_male_female():
    query_1 = {'gender': 'Male'}
    query_2 = {'gender': 'Female'}
    count_male = run_count(my_database, my_collection, query_1)
    count_female = run_count(my_database, my_collection, query_2)
    male_result = (count_male * 100) / (count_male + count_female)
    female_result = (count_female * 100) / (count_male + count_female)
    print(f"Male result : {male_result}")
    print(f"Female result : {female_result}")

def run_query(database, collection, query):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    client.close()
    results = db.get_collection(collection).find(query)
    return results

def update_in_user(database, collection, new_ip, name):
    client = MongoClient(MONGO_HOST)
    db = client [database]
    data = {'ip_address': new_ip}
    query = {'first_name': name}
    db.get_collection(collection).update_one(query, {"$set": data})
    client.close()
    result = run_query(database, collection, query)
    print(result)

def query_latitude_altitude(database, collection):
    query = {"$and": [{"latitude": {"$gt": 30}}, {"altitude": {"$lt": 10}}]}
    result = run_query(database,collection, query)
    get_print_from_cursor("and query", result)

def clean_collection (database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    db.get_collection(collection).delete_many()
    client.close()


my_database = "upsadb"
my_collection = "users"
import_json(my_database, my_collection)
insert_data(DATA, my_database, my_collection)
count_male_female()
update_in_user(my_database, my_collection, '109.150.230.156.24', 'Jervis')
query_latitude_altitude(my_database, my_collection)
