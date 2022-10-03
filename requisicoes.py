from cgitb import html
import contextlib
import http
from importlib.resources import contents
import site
import  requests
from bs4 import BeautifulSoup   

response = requests.get('https://g1.globo.com/')
print(response.content)
content = response.content
site = BeautifulSoup(content, 'html.parser')

noticia = site.find('div', attrs={'class': '_evt'})

#print(noticia.prettify())

titulo = site.find('a', attrs={'class': 'feed-post-link'})
print(titulo.text)



# print(site.prettify())

