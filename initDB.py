import psycopg2

from settings import *

def create_tables():
  conn = None
  try:
    conn = psycopg2.connect(dbname=DB_NAME, user=USER_NAME,
      host=HOST_NAME, password=HOST_PASS)
    cur = conn.cursor()
    cur.execute(QUERY_CHECK_TABLE_EXIST)
    exist = cur.fetchall()[0][0]
    
    if exist > 0:
      cur.execute(CMD_DELETE)
      conn.commit()
    cur.execute(CMD_CREATE)
    cur.close()
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()
 
if __name__ == '__main__':
    create_tables()
