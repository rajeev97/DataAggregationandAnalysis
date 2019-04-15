import csv

a = open('BernieSanders.csv')
b = open("BernieSanders.txt", "a")

for line in a:
	b.write(line)
b.close()