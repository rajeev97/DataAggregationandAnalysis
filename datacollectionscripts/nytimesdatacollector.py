from nytimesarticle import articleAPI
import requests
from bs4 import BeautifulSoup


def filecontentgenerator(url,count):
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html.parser')
	soup.prettify()
	a=len(soup.find_all('p',class_="css-1ygdjhk evys1bk0"))
	b=soup.find_all('p',class_="css-1ygdjhk evys1bk0")
<<<<<<< HEAD
	f=open("../data/nytimesSanders.txt","a")
=======
	f=open("../data/nytimescontent2.txt","a")
>>>>>>> de268e4993108de160f331a706c430e36f3da704
	for i in range(a):
		f.write(b[i].get_text())
		f.write("\n")
	f.close()




api=articleAPI("mAGYg4HiX3Oufv8FQbVddaKhguEAhRGZ")
pageno=1
count=0
while pageno<=100:
<<<<<<< HEAD
	articles=api.search(q="Bernie Sanders",begin_date=20190101,page=pageno)
=======
	articles=api.search(q="Hillary Clinton",begin_date=20190101,page=pageno)
>>>>>>> de268e4993108de160f331a706c430e36f3da704
	urls=[]
	for i in articles['response']['docs']:
		urls.append(i['web_url'])
		count=count+1
	print(urls)
	print(count)
	for i in range(len(urls)):
		filecontentgenerator(urls[i],i)
	pageno=pageno+1

