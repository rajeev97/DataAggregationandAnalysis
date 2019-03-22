import tweepy
import time
import csv

consumer_key='oZhRd76Den7k8shzfvnjTJ8vQ' 
consumer_secret='NXADm85cDwHGdehXcEt1xtZUWTQA2k64XEXmPwO7X3DnJNKRYD'
access_key='1097308522356850688-wzepBEyxq6KN6ZlLRLAmjfFLTFCGKX'
access_secret='NS19q7vAfc7JiTxhYNIl6ymLPFaKN8VveE1RdNBIORfpG'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)


def tweet_extraction(query, num):
	tweets=api.search(query, count=num)
	csvfile=open('../data/tweetdata.csv','a')
	csvWriter=csv.writer(csvfile)
	for tweet in tweets:
		if tweet.retweeted==False and 'RT @' not in tweet.text:
			csvWriter.writerow([tweet.text.encode('utf-8')])
	csvfile.close()

tweet_extraction("Trump",20000)

