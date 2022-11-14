import requests
import re, json
from bs4 import BeautifulSoup

URL = "https://www.mediamarkt.com.tr/tr/category/_cep-telefonlar%C4%B1-504171.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="category")

test = '<script>var product1218181 = {"name":"XIAOMI Poco X3 Pro 256 GB Ak?ll? Telefon Bronz","id":"1218181","price":"5799.00","brand":"XIAOMI","ean":"6934177738371","dimension25":"InStock","dimension26":11.90,"dimension24":18.00,"category":"Telefon","dimension9":"Cep Telefonlar?","dimension10":"Android Telefonlar"};</script>'

pattern = re.compile('.*?var product1218181 = (.*?);.*?')
match = pattern.match(test)
if match is not None:
    data = json.loads(match.groups()[0])
    for key, value in data.items():
        print(key, ":", value)