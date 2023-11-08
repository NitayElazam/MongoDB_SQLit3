from pymongo import *  # Import the pymongo library

DB_connection = MongoClient("mongodb://localhost:27017/")  # Connect to the database

clients_DB = DB_connection["Clients"]  # Create database with the name "Clients"
premiumClientsCollection = clients_DB["Premium"]  # Create collection with the name "Premium"

currentQuery = {"Client Age": 20}  # Current value of the client
newData = {"$set": {"Client Age": 21}}  # New data to update

premiumClientsCollection.update_one(currentQuery, newData)  # Update the data
