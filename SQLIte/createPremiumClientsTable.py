from sqlite3 import *  # Import the sqlite3 library

connection = connect("./Clients.db")  # Connect to the database by the path
cursor = connection.cursor()  # Create the cursor

# Create table command
command = """
CREATE TABLE PremiumClients (
    name varchar(255) NOT NULL,
    age int NOT NULL
)
"""

cursor.execute(command)  # Run the command
connection.commit()  # Commit the command