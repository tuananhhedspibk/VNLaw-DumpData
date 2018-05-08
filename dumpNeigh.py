from settings import *
import psycopg2

def load_data_ids():
  data_list = []
  with open(A_IDS_FILE_NAME) as f_p:
    for line in f_p:
      data_list.append(line.strip())
  f_p.close()

  return data_list

def load_data_neighbors(a_ids):
  data = []
  with open(INPUT_NEIGHBOR_FILE_NAME) as f_p:
    for line in f_p:
      line_splited = line.split(" ")
      a_neigh = a_ids[int(line_splited[1])] + " " + a_ids[int(line_splited[2])] + " " + a_ids[int(line_splited[3])] + " " + a_ids[int(line_splited[4])] + " " + a_ids[int(line_splited[5])]
      tmp = {a_ids[int(line_splited[0])]: a_neigh}
      data.append(tmp)
  return data

def dump_data(articles_neighbors):
  db_con = psycopg2.connect(dbname=DB_NAME, user=USER_NAME,
    host=HOST_NAME, password=HOST_PASS)
  cur = db_con.cursor()

  for article_neighbors in articles_neighbors:
    cur.execute(QUERY_INSERT_NEIGHBORS, (article_neighbors.values()[0], article_neighbors.keys()[0]))

  db_con.commit()
  db_con.close()
  cur.close()

def main():
  a_ids = load_data_ids()
  a_neighbors = load_data_neighbors(a_ids)
  dump_data(a_neighbors)

if __name__ == "__main__":
  main()
