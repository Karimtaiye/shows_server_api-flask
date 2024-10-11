import sqlite3

def db_connect(path):
    try:
        conn = sqlite3.connect(path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        print(f"DB Connection Successful!")
        return conn
    except sqlite3.OperationalError as err:
        print(f"DB Connection failed: {err}")
        conn.close()