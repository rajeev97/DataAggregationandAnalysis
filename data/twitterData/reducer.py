from operator import itemgetter
import sys

current_word = None
current_count = 1
word = None

file = open("temp.txt")

file2 = open("new.txt", "a")

for line in file:

    line = line.strip()

    wordpair, count = line.split('\t', 1)
    print(wordpair)
    #try:
     #   count = int(count)
    #except ValueError:
     #   continue
    print(count)
    if current_word == wordpair:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
            #file2.write('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = wordpair

if current_word == wordpair:
    print ('%s\t%s' % (current_word, current_count))
    #file2.write('%s\t%s' % (current_word, current_count))