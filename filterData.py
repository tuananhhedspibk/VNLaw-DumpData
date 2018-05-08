# -*- coding: utf-8 -*-

from settings import *

def remove_sign_of_vietnamese_char(input):
  vietnameseSign = [
    "aAeEoOuUiIdDyY",
    "áàạảãâấầậẩẫăắằặẳẵ",
    "ÁÀẠẢÃÂẤẦẬẨẪĂẮẰẶẲẴ",
    "éèẹẻẽêếềệểễ",
    "ÉÈẸẺẼÊẾỀỆỂỄ",
    "óòọỏõôốồộổỗơớờợởỡ",
    "ÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠ",
    "úùụủũưứừựửữ",
    "ÚÙỤỦŨƯỨỪỰỬỮ",
    "íìịỉĩ",
    "ÍÌỊỈĨ",
    "đ",
    "Đ",
    "ýỳỵỷỹ",
    "ÝỲỴỶỸ"
  ]

  input = input.lower()
  for i in range(1, len(vietnameseSign)):
    for j in range(len(vietnameseSign[i])):
      input = input.replace(vietnameseSign[i][j], vietnameseSign[0][i - 1])

  return input

def check_quote_symbol(input_str):
  if "(" in input_str:
    if ")" not in input_str:
      input_str = input_str.replace("(", " ")
      input_str = input_str.strip()

  if ")" in input_str:
    if "(" not in input_str:
      input_str = input_str.replace(")", " ")
      input_str = input_str.strip()

  return input_str.strip()

def remove_under_score(input_str):
  return input_str.replace("_", " ")

def load_data_graph():
  data_list = []
  with open(INPUT_KEYWORDS_TOPICS_DIS_SRC_FILE_NAME) as f_p:
    for line in f_p:
      a_data = line.split("@")[1].strip()
      a_kw = line.split("@")[0]
      article = {a_kw: a_data}
      data_list.append(article)
  f_p.close()

  return data_list

def filter_data_graph(data):
  f_p = open(INPUT_KEYWORDS_TOPICS_DIS_FILE_NAME, "w")
  for a_data in data:
    kw = a_data.keys()[0]
    kw = remove_under_score(kw)
    kw = check_quote_symbol(kw)
    tmp_kw = kw
    for symbol in FORBIDEN_SYMBOL_TOPICS:
      tmp_kw = "".join(tmp_kw.split(symbol))
    tmp_kw = remove_sign_of_vietnamese_char(tmp_kw)
    if tmp_kw.isalpha():
      f_p.write(kw + "@" + a_data.values()[0] + "\n")
    else:
      print kw

  f_p.close()

def load_data_a_topics():
  data_list = []
  with open(INPUT_TOPICS_PRO_SRC_FILE_NAME) as f_p:
    for line in f_p:
      a_data = line.split("@")[1]
      a_id = line.split("@")[0]
      article = {a_id: a_data}
      data_list.append(article)
  f_p.close()

  return data_list

def filter_data_a_topics(data):
  f_p = open(INPUT_TOPICS_PRO_FILE_NAME, "w")
  for a_data in data:
    topics_list = a_data.values()[0]
    filtered_topics = []
    topics_list_splited = topics_list.split("#")
    for topic in topics_list_splited:
      topic = check_quote_symbol(topic)
      tmp_topic = topic
      for symbol in FORBIDEN_SYMBOL_TOPICS:
        tmp_topic = "".join(tmp_topic.split(symbol))
      tmp_topic = remove_sign_of_vietnamese_char(tmp_topic)
      if tmp_topic.isalpha():
        filtered_topics.append(topic)
    if len(filtered_topics) > 0:
      f_p.write(a_data.keys()[0] + "@")
      ct = 0
      for topic in filtered_topics:
        if ct == len(filtered_topics) - 1:
          f_p.write(topic + "\n")
        else:
          f_p.write(topic + "#")
          ct += 1
  f_p.close()

def main():
  data = load_data_a_topics()
  filter_data_a_topics(data)
  data_graph = load_data_graph()
  filter_data_graph(data_graph)

if __name__ == '__main__':
  main()
