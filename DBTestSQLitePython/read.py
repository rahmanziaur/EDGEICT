import sqlite3

# Connect to the database
conn = sqlite3.connect('tt.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to retrieve all records
select_query = '''
SELECT * FROM users;
'''

# Execute the SQL command
cursor.execute(select_query)

# Fetch all the records
records = cursor.fetchall()

# Print the records
print("All records in the users table:")
for record in records:
    print(record)

# Close the connection
conn.close()
