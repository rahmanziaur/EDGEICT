import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('tt.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
'''

# Execute the SQL command
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table created successfully in tt.db")
