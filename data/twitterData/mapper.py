import sys

file = open("TestClean.txt")

top_ten_words = ["BernieSanders", "HillaryClinton", "httpst", "Trump", "Obama", "people", "say", "get", "like", "Bernie"]

file2 = open("temp.txt", "a")
for line in file:
	words = line.split()
	for i in range(len(words)-1):
		if words[i] in top_ten_words:
			for j in range(i+1,len(words)):
				file2.write("%s|%s\t%s" % (words[i],words[j], 1))
				#print("%s|%s\t%s" % (words[i],words[j], 1))


file.close()
file2.close()