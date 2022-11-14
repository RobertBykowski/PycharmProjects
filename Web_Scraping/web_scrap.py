from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/category/development').text
soup = BeautifulSoup(source, "html.parser")

# article = soup.find('article')
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='enrty-content').p.text
    print(summary)


