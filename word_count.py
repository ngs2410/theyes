# A quick and simple script to count word occurrences in the Product JSON
#
from collections import Counter

from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import requests


PRODUCT_DATA_URL = "https://raw.githubusercontent.com/chenlh0/product-classification-challenge/master/product_data.json"
DESCRIPTION = 'description'

word_count = Counter()
stop_tokens = set(stopwords.words('english')) | {',', '%', '.', ':', '-', "'", "/", "''"}

for d in requests.get(PRODUCT_DATA_URL).json():
	raw_desc = d.get(DESCRIPTION, '')
	if raw_desc:
		desc = BeautifulSoup(raw_desc).get_text().lower()
		tokens = set(nltk.word_tokenize(desc)) - stop_tokens
		word_count.update(tokens)

for token, count in word_count.most_common():
	print(token, count)
