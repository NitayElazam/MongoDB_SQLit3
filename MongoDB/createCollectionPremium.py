from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
premiumClientsCollection = clients_DB["Premium"]  # Create collection with the name "Premium"

premiumClientsList = [   # Create list of all the premium clients
    {"Client Name": "Haim", "Client Age": 20},  # First client
    {"Client Name": "David", "Client Age": 24}, # Second client
    {"Client Name": "Yosi", "Client Age": 25}   # Third client
]

premiumClientsCollection.insert_many(premiumClientsList)  # Insert all the client to the collection "Premium"
