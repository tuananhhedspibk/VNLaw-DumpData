# -*- coding: utf-8 -*-

INPUT_NEIGHBOR_FILE_NAME = "./input/neighbor_articles.txt"
INPUT_TOPICS_PRO_FILE_NAME = "./input/phrase_topics_pro_cleaned.txt"
INPUT_TOPICS_PRO_SRC_FILE_NAME = "./input/phrase_topics_pro.txt"
INPUT_ARTICLE_FILE_NAME = "./input/articles.tsv"
INPUT_KEYWORDS_TOPICS_DIS_SRC_FILE_NAME = "./input/keyword_topics_distribution.txt"
INPUT_KEYWORDS_TOPICS_DIS_FILE_NAME = "./input/keyword_topics_distribution_cleaned.txt"
A_IDS_FILE_NAME = "./input/a_ids.txt"

REDUNDANT_SYMBOL = ["\\t", "\\r", "\\n", "##", "\\", "”",
  "**___________________**", "**", "---", "_", "|", "…",
  "---|---|---|---|---"]

REDUNDANT_PATTERN = ["[a-z]\)", "đ\)", "&amp",
  "(\d+\/)*([A-Z\d\%\-a-z]+)+(\&[a-z]+\;([a-z]+\=[A-Za-z\d]+)+)+\"",
  "([a-z]+\=\"[a-z_]+\"\&[a-z;]+)+",
  "((\)\;)+[a-z\-\:\;\"]+)+", "([a-z]+\=\".*\-)+",
  "(right:[a-z\d]+\;)(color\:[a-z\(\d\,\s]+)"]

REDUNDANT_STRING_PATTERN = ["điều \d{1,2}", "khoản \d{1,2}",
  "chương [ivxlcdm]+", "điểm \d{1,2}",
  "phần thứ [a-zâấưăáảáíờộơ ]+", "mục \d{1,2}",
  "cộng hoà xã hội chủ nghĩa việt nam", "độc lập - tự do - hạnh phúc",
  "\d{1,2}\\\.", "[\w]\)", "đ\)"]

FORBIDEN_SYMBOL_TOPICS = [" ", "(", ")", "-"]

DB_NAME = "test_lda"
USER_NAME = "anhtt"
HOST_NAME = "localhost"
HOST_PASS = "12345678"

QUERY_CHECK_EXIST = """
  SELECT exists(SELECT 1 from articles where id=(%s))
"""

QUERY_INSERT_TOPICS = """
  UPDATE articles SET topics = (%s) WHERE id = (%s);
"""

QUERY_INSERT_NEIGHBORS = """
  UPDATE articles SET neighbors = (%s) WHERE id = (%s);
"""

QUERY_INSERT_ARTICLES = """
  INSERT INTO articles(id, title, content, full_html, index_html,
    numerical_symbol, public_day, day_report, article_type, source, agency_issued, the_signer, signer_title,
    scope, effect_day, effect_status, count_click, topics, neighbors, created_at, updated_at)
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""
