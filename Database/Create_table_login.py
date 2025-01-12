import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0946192332"
)

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE TESTd")

