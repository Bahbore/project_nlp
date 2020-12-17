import nltk
from tokenize import String
import string
from nltk.book import text9
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
# < All library u need in the project i think >

# let's start .... list from stop words :-
stop_words_list =list (stopwords.words('english'))
# list of All punctuation :-
Punctuation_List =list( string.punctuation )
# List of All words in Broun Corpuse & splitting it without Any operation :-
list_Brown_Word = brown.words(categories = 'science_fiction')
# initialize string text of brown corpuse :-
Brown_text = " ".join(list_Brown_Word)
# List of all segments of Brown corpuse (science_fiction)
Brown_segments =  sent_tokenize(Brown_text)
# list of all word in Brown corpuse without stop words
txt_without_stopwords =[]
for word in list_Brown_Word:
    if word not in  stop_words_list :
        txt_without_stopwords.append(word)
# stemming operation on all words without stop words By Snow_Ball_Steammer
Steammer = SnowballStemmer('english' , ignore_stopwords= True)
stemming_list = []
for w in txt_without_stopwords:
    if w not in Punctuation_List:
        stemming_list.append(Steammer.stem(w))


