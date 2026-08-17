import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db1"
)

if conn.is_connected():
    print("Connected to MySQL successfully!")

cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()