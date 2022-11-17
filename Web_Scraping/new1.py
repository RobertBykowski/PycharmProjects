import requests
from bs4 import BeautifulSoup


url = 'https://atp-ejendomme.dk/find-lejemaal/christiansbro/'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

for k, v in zip(soup.select('.fact_title'), soup.select('.fact_answer')):
    print('{:<25} {}'.format(k.text, v.text))