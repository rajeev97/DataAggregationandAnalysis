import tweepy
import time
import csv

consumer_key='oZhRd76Den7k8shzfvnjTJ8vQ' 
consumer_secret='NXADm85cDwHGdehXcEt1xtZUWTQA2k64XEXmPwO7X3DnJNKRYD'
access_key='1097308522356850688-wzepBEyxq6KN6ZlLRLAmjfFLTFCGKX'
access_secret='NS19q7vAfc7JiTxhYNIl6ymLPFaKN8VveE1RdNBIORfpG'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


def tweet_extraction(filename,query, num):
	tweet_count=0
	#tweets=api.search(query, count=num)
	cursor= tweepy.Cursor(api.search,q=query,count=num,tweet_mode='extended',since="2019-01-01", lang="en").items()#, #date='2017-11-13', days_ago=9).items(5)
	csvfile=open(filename,'a')
	csvWriter=csv.writer(csvfile)
	for tweet in cursor:
		if tweet.retweeted==False and 'RT @' not in tweet.full_text:
			csvWriter.writerow([tweet.full_text])
			print(tweet.full_text)
			tweet_count=tweet_count+1
	print(tweet_count)
	csvfile.close()

#tweet_extraction("Obama",20000)

