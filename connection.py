import psycopg2
from config import config

usuario = ""

def funUsuario(valor):
    global usuario
    usuario = valor
    
def connect(query):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        sqlquey = f"set my.app_user = '{usuario}'"
        
        cur.execute(sqlquey)
        try:
            results = cur.fetchall()
        except:
            results = ""
        
        conn.commit()
        
        
        sqlquey = query
        
        cur.execute(sqlquey)
        try:
            results = cur.fetchall()
        except:
            results = ""
        
        conn.commit()
        cur.close()
        
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def column_names(query):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        sqlquey = query
        
        cur.execute(sqlquey)
        column_names = [desc[0] for desc in cur.description]
        
        conn.commit()
        cur.close()
        
        return column_names
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()