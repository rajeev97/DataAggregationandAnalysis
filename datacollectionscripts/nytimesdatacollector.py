from nytimesarticle import articleAPI
import requests,json

api=articleAPI("Yj748LqEodhbdLaVjRgbvN5aQQQqL57v")
articles=api.search(q="Trump",begin_date=20190101)
urls=[]
for i in articles['response']['docs']:
	urls.append(i['web_url'])

r=requests.get(urls[0])

