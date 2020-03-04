import requests
from bs4 import BeautifulSoup

URL = 'https://www.rosalindfranklin.edu/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
newsBlurb = soup.find(class_='header_news_description')
newsLink = soup.find(class_='header_news_buttons')

link = newsLink.find('a')['href']

print(newsBlurb.find('p').prettify())
print(f"learn more here: {link}\n")