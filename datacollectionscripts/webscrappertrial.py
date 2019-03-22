from bs4 import BeautifulSoup
import requests


r=requests.get("https://www.nytimes.com/2019/03/05/books/review/victor-davis-hanson-case-for-trump.html")
soup=BeautifulSoup(r.content,'html.parser')
soup.prettify()
a=len(soup.find_all('p',class_="css-1ygdjhk evys1bk0"))
b=soup.find_all('p',class_="css-1ygdjhk evys1bk0")
f=open("nytimescontent.txt","a")
for i in range(a):
	f.write(b[i].get_text())
f.close()



