import csv
import os

filenames=["../data/HillaryClintondata.csv","../data/trumpData.csv","../data/Obamadata.csv","../data/BernieSanders.csv"]
tweets=[]
original_count=0
for file in filenames:
	with open(file,"r") as csv_file:
		csv_reader=csv.reader(csv_file)
		for tweet in csv_reader:
			original_count=original_count+1
			if tweet not in tweets:
				tweets.append(tweet)
print("Original Number of Tweets is"+str(original_count))

with open("../data/UniqueTweetsFinal.csv",'a') as csv_file:
	csv_writer=csv.writer(csv_file)
	for tweet_count,tweet in enumerate(tweets):
		csv_writer.writerow([tweet])
	print("After removing duplicates"+str(tweet_count+1))
csv_file.close()
