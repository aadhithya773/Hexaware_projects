import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from util.DbpropertyUtil import getPropertyString

class DBConnUtil:

    @staticmethod
    def get_connection():
            try:
                conn_str = getPropertyString("resources/db.properties")
                print("connection string:",conn_str)  # you can print connection string if you want
                DBConnUtil.connection = pyodbc.connect(conn_str)
                print("Database connected successfully!")
                return DBConnUtil.connection    
            except Exception as e:
                print("Error connecting to database:", e)
                return None
