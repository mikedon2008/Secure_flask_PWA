import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
connection = sqlite3.Connection("LoginData.db")
cursor = connection.cursor()

# Create USERS table if it doesn't already exist
cmd1 = """CREATE TABLE IF NOT EXISTS USERS(
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50) NOT NULL)"""
cursor.execute(cmd1)

# Insert a sample user into the USERS table
cmd2 = """INSERT INTO USERS (first_name, last_name, email, password) VALUES
            ('tester', 'test', 'tester@gmail.com', 'tester')"""
cursor.execute(cmd2)
connection.commit()

# Retrieve and print all records from the USERS table
ans = cursor.execute("SELECT * FROM USERS").fetchall()
for i in ans:
    print(i)

