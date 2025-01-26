import os
from dotenv import load_dotenv
import mysql.connector


load_dotenv()

def get_db_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER',),
            password=os.getenv('DB_PASSWORD',),
            database=os.getenv('DB_NAME', 'employee_management')
        )
    except mysql.connector.Error as e:
        raise RuntimeError(f"Database connection error: {e}")
