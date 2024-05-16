# Task 1: Setting Up the Flask Environment and Database Connection

import mysql.connector
from mysql.connector import Error

# Database configuration
db_name = 'library_management_sys'
user = "root"
password = 'Martinez!1996'
host = 'localhost'

# Establish a database connection
def db_connection():
    try:
        #Attempting connection
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print("Connection to MySQL database successful!")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

