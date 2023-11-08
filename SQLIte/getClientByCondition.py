from sqlite3 import *  # Import the sqlite3 library

connection = connect("./Clients.db")  # Connect to the database by the path
cursor = connection.cursor()  # Create the cursor

# View the content from the table by condition
command = """
SELECT * FROM RegularClients WHERE age >= 20
"""

result = cursor.execute(command)  # Run the command

for line in result.fetchall():  # Run on the command result
    print(f"Client > {line}")   # Print the current client