import nltk, re
from nltk.tokenize import word_tokenize
# importing ngrams module from nltk
from nltk.util import ngrams
from collections import Counter
sentence = "I am having my breakfast"


cleaned = re.sub('\W+', ' ', sentence ).lower()

print(cleaned)
