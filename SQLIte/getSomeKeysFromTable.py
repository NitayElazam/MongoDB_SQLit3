from sqlite3 import *  # Import the sqlite3 library

connection = connect("Clients.db")  # Connect to the database by the path
cursor = connection.cursor()  # Create the cursor

# Get some keys from table
command = """
SELECT name, age FROM PremiumClients
"""

result = cursor.execute(command)  # Run the command

for line in result.fetchall():  # Run on command result
    print(f"Client > {line}")   # Print current client