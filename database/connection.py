from mysql import connector


config = {
    'user': 'root03',
    'password': '1234',
    'host': '192.168.0.141',
    'database': 'monitoreo_trabajo_02',
}

def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}" )
    return conn