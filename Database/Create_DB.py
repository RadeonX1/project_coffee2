import mysql.connector
from mysql.connector import (connection)

db = connection.MySQLConnection(user='root',password='0946192332',host='127.0.0.1')

db.close()
