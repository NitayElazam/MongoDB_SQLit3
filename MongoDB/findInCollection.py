from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
regularClientsCollection = clients_DB["Regular"]  # Create collection with the name "Regular"

print(len(list(regularClientsCollection.find())))

for regularClient in regularClientsCollection.find():  # Run on regular clients list
    print(f"Client > {regularClient}")  # Print the current client
