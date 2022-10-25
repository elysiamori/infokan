import mysql.connector

db = mysql.connector.connect(
 host="localhost:8080",
  user="root",
  password=""
)

print(db)
