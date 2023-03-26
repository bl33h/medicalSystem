import psycopg2
from config import config

def connect(query):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        sqlquey = query
        
        cur.execute(sqlquey)
        results = cur.fetchall()
        
        conn.commit()
        cur.close()
        
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()