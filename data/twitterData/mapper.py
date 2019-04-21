import sys


top_ten_words = ["BernieSanders", "HillaryClinton", "go", "Trump", "Obama", "people", "say", "get", "like", "Bernie"]


for line in sys.stdin:
	line = line.strip()
	words = line.split()
	for i in range(len(words)-1):
		if words[i] in top_ten_words:
			for j in range(i+1,len(words)):
				if(words[j] != words[i]):
					print("%s|%s\t%s" % (words[i],words[j], 1))


file.close()
file2.close()
