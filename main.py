import requests
from bs4 import BeautifulSoup
import smtplib
import imdb
import datetime

url="https://en.wikipedia.org/wiki/Main_Page"
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

title=soup.title
#print(type(title))
#print(type(title.string))
#print(type(soup))
#com="<p><!-- this is a comment --></p>"
#soup2=BeautifulSoup(com)
#print(type(soup2.p.string))
#exit()

paras=soup.findAll('p')
#print(paras)

#print(soup.find('p'))
#print(soup.find('p')['class'])
#print(soup.find('p').get_text())

anchors=soup.findAll('a')
#print(anchors)
#for link in anchors:
#        linktext='https://en.wikipedia.org'+link.get('href')
#        print(linktext)

x=soup.find(id="vector-main-menu-dropdown")
#for elem in x.stripped_strings:
#    print(elem)
#print(x.parent.name)
#for elem in x.parents:
#    print(elem.name)
#print(x.nextSibling)
#print(x.previousSibling)

soup3 = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup3.b
#tag.name = "blockquote"
#tag['class'] = 'verybold'
#tag['id'] = 1
#print(tag)
#del tag['class']
#del tag['id']
#print(tag)

#markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
#soup = BeautifulSoup(markup, 'html.parser')
#tag = soup.a
#tag.string = "New link text."
#print(tag)

#for img in soup.findAll('img'):
#    print(img.get('src'))

data = ''
#f = open("E:/test1.txt", "w")
#for data in soup.find("p"):
#    x = data.get_text()
#    f.writelines(x)
#f.close()

data = soup.find('p').get_text().encode('utf-8').strip()
#smt = smtplib.SMTP('smtp.gmail.com',587)
#smt.ehlo()
#smt.starttls()
#smt.login('bauraiayush733@gmail.com','rcmxoubuovzxtedk')
#print("login success!")
#smt.sendmail('bauraiayush733@gmail.com','bauraiayush733@gmail.com',f'Subject: Web Scraped Wikipedia using python\n\n {data}')
#smt.quit()

#moviesdb=imdb.IMDb()
#movies=moviesdb.search_movie('Conjuring')
#for movie in movies:
#    info=movie.getID()
#    movie=moviesdb.get_movie(info)
#    title=movie['title']
#    year=movie['year']
#    rating=movie['rating']
#    plot=movie['plot outline']
#    if year < int(datetime.datetime.now().strftime("%Y")):
#        print(f'{title} was released in {year} has IMDB rating of {rating}.\nThe plot summary of movie is{plot}')
#    else:
#        print(f'{title}will release in {year} has IMDB rating of {rating}.\nThe plot summary of movie is{plot}')