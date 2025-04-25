import configparser

class DBPropertyUtil:
    @staticmethod
    def get_db_params(file_name):
        config = configparser.ConfigParser()
        config.read(file_name)
        return {
            "server": config.get("database", "server"),
            "database": config.get("database", "database"),
            "driver": config.get("database", "driver")
        }
