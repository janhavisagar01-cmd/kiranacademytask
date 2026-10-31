import mysql.connector
from config import DB_CONFIG

def execute(sql, params=(), fetch=False):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(sql, params)
        result = cur.fetchall() if fetch else cur.lastrowid
        if not fetch:
            conn.commit()
        return result
    finally:
        cur.close()
        conn.close()
