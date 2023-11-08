from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
regularClientsCollection = clients_DB["Regular"]  # Create collection with the name "Regular"

condition = {"_id": 0, "Client Name": 1, "Client Age": 1}  # The keys condition

for regularClient in regularClientsCollection.find({}, condition):  # Run on regular clients list
    print(f"Client > {regularClient}")  # Print the current client
