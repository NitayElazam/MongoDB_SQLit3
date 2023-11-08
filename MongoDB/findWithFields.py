from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
regularClientsCollection = clients_DB["Regular"]  # Create collection with the name "Regular"

findQuery = {"Client Name": "Yair"}  # Query condition

result = regularClientsCollection.find(findQuery)  # Find all the clients by the condition

for client in result:  # Run on the list
    print(f"Client > {client}")  # Print the current client
