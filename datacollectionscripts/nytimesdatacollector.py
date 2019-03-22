from nytimesarticle import articleAPI
import requests
from bs4 import BeautifulSoup


def filecontentgenerator(url,count):
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html.parser')
	soup.prettify()
	a=len(soup.find_all('p',class_="css-1ygdjhk evys1bk0"))
	b=soup.find_all('p',class_="css-1ygdjhk evys1bk0")
	f=open("../data/nytimescontent.txt","a")
	for i in range(a):
		f.write(b[i].get_text())
	f.close()




api=articleAPI("Yj748LqEodhbdLaVjRgbvN5aQQQqL57v")
articles=api.search(q="Trump",begin_date=20190101)
urls=[]
for i in articles['response']['docs']:
	urls.append(i['web_url'])

for i in range(len(urls)):
	filecontentgenerator(urls[i],i)

