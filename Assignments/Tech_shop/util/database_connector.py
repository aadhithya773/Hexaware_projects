# util/DatabaseConnector.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc

class DatabaseConnector:
    def __init__(self):
        self.conn = None

    def open_connection(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=localhost;'
                'DATABASE=tech_shop;'
                'Trusted_Connection=yes;'
            )
            return self.conn
        except Exception as e:
            print(f"Error opening DB connection: {e}")
            return None

    def close_connection(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Error closing DB connection: {e}")
import pyodbc
from util.Dbpropertyutil import DBPropertyUtil

class DatabaseConnector:
    def __init__(self, config_file="db.properties"):
        self.conn = None
        self.connection_string = DBPropertyUtil.get_connection_string(config_file)

    def open_connection(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            return self.conn
        except Exception as e:
            print(f"Error opening DB connection: {e}")
            return None

    def close_connection(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Error closing DB connection: {e}")
