import string
import regex as re
import nltk 
from nltk.stem import PorterStemmer

stopword = nltk.corpus.stopwords.words('english')
ps = PorterStemmer()

def remove_punct(text):
	text  = "".join([char for char in text if char not in string.punctuation])
	text = re.sub('\p{P}+', '', text)
	return text
def remove_stopwords(text):
	words = text.split(" ")
	for i in range(len(words)):
		if words[i] not in stopword:
			words[i] = words[i]
		else:
			words[i] = ""
	return words
def fix_period_indent(text):
	l = list(text)
	for i in range(len(l)):
		if l[i] == '.':
			l[i] = ' '
		else:
			l[i] = l[i]
	return l
def stemming(text):
	words = text.split(" ")
	for i in range(len(words)):
			words[i] = ps.stem(words[i])
	return words
file = open("nytimesTrump.txt")
newfile = open("nytimesTrump_clean.txt", "w")
filestring = file.read()
s = fix_period_indent(filestring)
no_punct= remove_punct(s)
no_stop = ' '.join(remove_stopwords(no_punct))
string = ' '.join(stemming(no_stop))
newfile.write(string)


	