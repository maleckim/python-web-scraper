import requests
import json
import sys
import importlib
from bs4 import BeautifulSoup


URL = 'https://www.rosalindfranklin.edu/'
page = requests.get(URL)

newsObj = []

soup = BeautifulSoup(page.content, 'html.parser')
newsBlurb = soup.find(class_='header_news_description')
newsLink = soup.find(class_='header_news_buttons')

link = newsLink.find('a')['href']

newsObj.append({
  'newsblurb': newsBlurb.find('p').text,
  'link': link
  })

with open('news.json','w') as outfile:
  json.dump(newsObj, outfile)

with open('news.json','r') as n:
  news = json.load(n)

for n in news:
  print(n)

sys.stdout.flush()

# print(newsBlurb.find('p').text)
# print(f"learn more here: {link}\n")
