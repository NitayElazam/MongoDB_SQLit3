from sqlite3 import *  # Import the sqlite3 library

connection = connect("./Clients.db")  # Connect to the database by the path
cursor = connection.cursor()  # Create the cursor

# Insert into Regular Clients
command = """
INSERT INTO RegularClients (name, age)
VALUES ('Nitay', 17), ('Yosi', 22), ('Ilay', 20);
"""

res = cursor.execute(command)  # Execute the command
connection.commit()  # Commit the command