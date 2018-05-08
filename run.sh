#!/bin/bash

python initDB.py
python dumpArticlesData.py
python filterData.py
python dumpTopics.py
python dumpNeigh.py
