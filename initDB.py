import psycopg2

from settings import *

def create_tables():
  command_create = """
    CREATE TABLE articles (
      id TEXT NOT NULL,
      title TEXT,
      content TEXT,
      full_html TEXT,
      index_html TEXT,
      numerical_symbol TEXT,
      public_day DATE,
      day_report DATE,
      article_type TEXT,
      source TEXT,
      agency_issued TEXT,
      the_signer TEXT,
      signer_title TEXT,
      scope TEXT,
      effect_day DATE,
      effect_status TEXT,
      count_click INTEGER,
      topics TEXT,
      neighbors TEXT,
      created_at DATE,
      updated_at DATE,
      PRIMARY KEY (id)
    )
    """
  command_delete = """
      DROP TABLE articles
    """
  conn = None
  try:
    conn = psycopg2.connect(dbname=DB_NAME, user=USER_NAME,
      host=HOST_NAME, password=HOST_PASS)
    cur = conn.cursor()
    cur.execute(command_delete)
    conn.commit()
    cur.execute(command_create)
    cur.close()
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()
 
if __name__ == '__main__':
    create_tables()
