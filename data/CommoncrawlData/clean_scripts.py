import string
import regex as re
import nltk 
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stopword = nltk.corpus.stopwords.words('english')
ps = PorterStemmer()

wn = nltk.WordNetLemmatizer()


def remove_punct(text):
	text  = "".join([char for char in text if char not in string.punctuation])
	text = re.sub('\p{P}+', '', text)
	#text = re.sub('[0-9]+', '', text)
	return text
def remove_stopwords(text):
	words = text.split()
	finalwords = []
	for i in range(len(words)):
		if words[i].lower() not in stopword:
			#print(words[i])
			finalwords.append(words[i])
	return finalwords
def fix_period_indent(text):
	l = list(text)
	for i in range(len(l)):
		if l[i] == '.':
			l[i] = ' '
		else:
			l[i] = l[i]
	return l
def lemmatizer(text):
	word = text.split()
	for i in range(len(word)):
			word[i] = wn.lemmatize(word[i], pos = "v")
	return word
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')
file = open("COMMONCRAWLCONTENT.txt")
#newfile = open("UniqueTweets.txt", "a")
newfile = open("CommonCrawlClean.txt", "a")
#filestring = file.read()
for line in file:
	#print(line)
	#print(type(line))
	#line = ''.join(line.replace("\n", ""))
	s = fix_period_indent(line)
	no_punct= remove_punct(s)
	no_stop = ' '.join(remove_stopwords(no_punct))
	string_final = ' '.join(lemmatizer(no_stop))
	final = ' '.join(remove_stopwords(string_final))
	#print(string_final)
	string_final2 = deEmojify(final)
	#print("String after cleaning ",string_final)
	string_final2=string_final2.replace("httpst","")
	string_final2=string_final2.replace("http","")
	string_final2=string_final2.replace("https","")
	newfile.write(string_final2+"\n")
newfile.close()
