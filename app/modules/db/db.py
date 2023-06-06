import mysql.connector

def get_connection():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        database='db_books',
        password='admin1234'
    )
    return conexion