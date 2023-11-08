from sqlite3 import *  # Import the sqlite3 library

connection = connect("Clients.db")  # Connect to the database by the path
cursor = connection.cursor()  # Create the cursor

# Delete by condition
command = """
DELETE FROM RegularClients WHERE age < 20
"""

cursor.execute(command)  # Run command
connection.commit()  # Commit command
