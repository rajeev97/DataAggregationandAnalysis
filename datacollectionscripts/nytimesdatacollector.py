from nytimesarticle import articleAPI
import requests
from bs4 import BeautifulSoup


def filecontentgenerator(url,count):
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html.parser')
	soup.prettify()
	a=len(soup.find_all('p',class_="css-1ygdjhk evys1bk0"))
	b=soup.find_all('p',class_="css-1ygdjhk evys1bk0")
	f=open("../data/nytimescontent1.txt","a")
	for i in range(a):
		f.write(b[i].get_text())
		f.write("\n")
	f.close()




api=articleAPI("Yj748LqEodhbdLaVjRgbvN5aQQQqL57v")
pageno=1
while pageno<=100:
	articles=api.search(q="Trump",begin_date=20190101,page=pageno)
	urls=[]
	for i in articles['response']['docs']:
		urls.append(i['web_url'])
	print(urls)
	for i in range(len(urls)):
		filecontentgenerator(urls[i],i)
	pageno=pageno+1

