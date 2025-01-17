import sqlite3

# Connect to the database
conn = sqlite3.connect('tt.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to insert data
insert_query = '''
INSERT INTO users (id, name, email)
VALUES (?, ?, ?);
'''

# Data to be inserted
data = (101, 'Abdur Rahman', 'abrahman@gmail.com')

# Execute the SQL command
cursor.execute(insert_query, data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully into the users table.")
