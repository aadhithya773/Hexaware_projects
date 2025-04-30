import configparser

def getPropertyString(filepath):
    config = configparser.ConfigParser()
    config.read(filepath)

    try:
        driver = config.get('database', 'driver')
        server = config.get('database', 'server')
        database = config.get('database', 'database')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Missing property or section in File: {e}")
        raise

    # Build connection string
    conn_str = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return conn_str
