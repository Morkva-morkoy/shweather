import sqlite3

conn = sqlite3.connect('db.db')

print("Opened database successfully")
cursor = conn.execute("SELECT id, nickname, password, email, city FROM users")
conn.close()
print("Records created successfully")
