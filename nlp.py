
from nltk import word_tokenize
import nltk
from nltk.stem import PorterStemmer

import nltk
nltk.download('averaged_perceptron_tagger')


import nltk
nltk.download('maxent_ne_chunker')

from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
wd = WordNetLemmatizer()



from nltk import ne_chunk


import string





string = "Nice to meet you"



string_tokenize = nltk.word_tokenize(string)
print_word = [wd.lemmatize(string_tokenize)]
print(print_word)

#hurray you wrote nlp

# string_trigrams = list(nltk.trigrams(string))
# print(string_trigrams)




# # print(PorterStemmer().stem("dozing"))
# token_1 = "I am haing my dinner"
# token_sent = word_tokenize(token_1)


# for token in token_sent:
#     print(nltk.pos_tag([token]))



# ne_tag = "The US President stays in the WHITEHOUSE"


# ne_tag_tokenize = word_tokenize(ne_tag)
# ne_tag_tokenize_pos_tag = nltk.pos_tag(ne_tag_tokenize)


# print(ne_tag_tokenize_pos_tag)





# print(wd.lemmatize("having"))
