from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
premiumClientsCollection = clients_DB["Premium"]  # Create collection with the name "Premium"

allClients = premiumClientsCollection.find().limit(2)  # Get only the two clients from the list

for client in allClients:  # Run on the list
    print(f"Client > {client}")  # Print the current client
