import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.dbconnUtil import DBConnUtil
from util.Dbpropertyutil import DBPropertyUtil

def test_connection():
    conn_str = DBPropertyUtil.get_connection_string('db.properties')
    if not conn_str:
        print("Failed to generate connection string.")
        return

    connection = DBConnUtil.get_connection(conn_str)
    if connection:
        print("✅ Database connection successful!")
        connection.close()
    else:
        print("❌ Failed to connect to the database.")

if __name__ == "__main__":
    test_connection()
