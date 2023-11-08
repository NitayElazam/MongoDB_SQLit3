from sqlite3 import *  # Import the sqlite3 library

connection = connect("./Clients.db")  # Connect to the database by the path
cursor = connection.cursor()  # Create the cursor

# Insert into Premium Clients
command = """
INSERT INTO PremiumClients (name, age)
VALUES ('Haim', 22), ('David', 20), ('Moshe', 30);
"""

res = cursor.execute(command)  # Execute the command
connection.commit()  # Commit the command