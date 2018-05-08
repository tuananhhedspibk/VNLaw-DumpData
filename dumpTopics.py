from settings import *
import psycopg2

def load_data():
  data_list = []
  with open(INPUT_TOPICS_PRO_FILE_NAME) as f_p:
    for line in f_p:
      a_data = line.split("@")[1]
      a_id = line.split("@")[0]
      article = {a_id: a_data}
      data_list.append(article)
  f_p.close()

  return data_list

def dump_data(articles_topics):
  db_con = psycopg2.connect(dbname=DB_NAME, user=USER_NAME,
    host=HOST_NAME, password=HOST_PASS)
  cur = db_con.cursor()

  for article_topics in articles_topics:
    cur.execute(QUERY_INSERT_TOPICS, (article_topics.values()[0], article_topics.keys()[0]))

  db_con.commit()
  db_con.close()
  cur.close()

def main():
  articles_topics = load_data()
  dump_data(articles_topics)

if __name__ == "__main__":
  main()
