class DBPropertyUtil:
    @staticmethod
    def get_connection_string(file_path):
        try:
            props = {}
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        key, value = line.split("=", 1)
                        props[key.strip()] = value.strip()

            driver = props.get('driver', '{ODBC Driver 17 for SQL Server}')
            server = props.get('server', 'ASUS\SQLEXPRESS')
            database = props.get('database', 'tech_shop')
            trusted_connection = props.get('trusted_connection', 'yes')

            connection_string = (
                f"DRIVER={driver};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"Trusted_Connection={trusted_connection};"
            )
            return connection_string

        except Exception as e:
            print(f"Error reading DB config: {e}")
            return None
