import sqlite3

# Create a connection to a new database
conn = sqlite3.connect("tt.db")

# Close the connection
conn.close()
