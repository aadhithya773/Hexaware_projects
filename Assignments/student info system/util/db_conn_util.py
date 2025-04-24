import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(property_file='db.properties'):
        try:
            db_params = DBPropertyUtil.get_db_params(property_file)
            conn_str = (
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={db_params["server"]};'
                    f'DATABASE={db_params["database"]};'
                    f'Trusted_Connection=yes;'
                )

            connection = pyodbc.connect(conn_str)
            return connection

        except Exception as e:
            print("Database connection failed:", e)
            return None
