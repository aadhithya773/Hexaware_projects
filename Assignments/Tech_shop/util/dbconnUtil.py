import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection(conn_str):
        try:
            connection = pyodbc.connect(conn_str)
            return connection
        except Exception as e:
            print(f"❌ Error connecting to DB: {e}")
            return None
