import pyodbc
import os

class DBUtil:
    @staticmethod
    def get_connection():
        try:
            # Construct the path to the db.properties file
            prop_path = os.path.join(os.path.dirname(__file__), '../resources/db.properties')

            # Read the properties file
            props = {}
            with open(prop_path, 'r') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        props[key.strip()] = value.strip()

            # Build the connection string using those values
            conn_str = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={props.get('server')};"
                f"DATABASE={props.get('database')};"
                f"UID={props.get('username')};"
                f"PWD={props.get('password')};"
                f"Trusted_Connection={'yes' if props.get('trusted_connection', 'no').lower() == 'yes' else 'no'};"
            )

            # Create and return the connection
            return pyodbc.connect(conn_str)

        except Exception as e:
            print(f"Error while connecting to database: {e}")
            return None
