import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=ASUS\SQLEXPRESS;'
            'DATABASE=HM_bank;'
        )
        return conn
    except pyodbc.Error as e:
        print("Database connection failed:", e)
        raise
