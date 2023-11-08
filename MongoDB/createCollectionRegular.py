from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
regularClientsCollection = clients_DB["Regular"]  # Create collection with the name "Regular"

regularClientsList = [   # Create list of all the regular clients
    {"Client Name": "Nitay", "Client Age": 17},  # First client
    {"Client Name": "Yair", "Client Age": 20}, # Second client
    {"Client Name": "Ilay", "Client Age": 30}   # Third client
]

regularClientsCollection.insert_many(regularClientsList)  # Insert all the client to the collection "Regular"
