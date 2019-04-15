import csv

a = open('UniqueTweetsFinal.csv')
b = open("UniqueTweetsFinal.txt", "a")

for line in a:
	b.write(line)
b.close()