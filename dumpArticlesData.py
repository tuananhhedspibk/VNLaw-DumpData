from settings import *
import psycopg2

def load_data():
  a_data_list = []
  with open(INPUT_ARTICLE_FILE_NAME) as f_p:
    for line in f_p:
      a_data_list.append(line.strip())
  return a_data_list

def dump_data(articles_data):
  db_con = psycopg2.connect(dbname=DB_NAME, user=USER_NAME,
    host=HOST_NAME, password=HOST_PASS)
  cur = db_con.cursor()
  for a_data in articles_data:
    a_data_splited = a_data.split("\t")
    cur.execute(QUERY_CHECK_EXIST, (a_data_splited[0],))
    exist = cur.fetchall()[0][0]
    if not exist:
      cur.execute(QUERY_INSERT_ARTICLES, (a_data_splited[0], a_data_splited[1], a_data_splited[2],
        a_data_splited[3], a_data_splited[4], a_data_splited[5], a_data_splited[6], a_data_splited[7],
        a_data_splited[8], a_data_splited[9], a_data_splited[10], a_data_splited[11], a_data_splited[12],
        a_data_splited[13], a_data_splited[14], a_data_splited[15], a_data_splited[16], '', '', a_data_splited[17], a_data_splited[18]))
  db_con.commit()

  db_con.close()
  cur.close()

def main():
  articles_data = load_data()
  dump_data(articles_data)

if __name__ == "__main__":
  main()
