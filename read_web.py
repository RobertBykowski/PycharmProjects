import urllib.request
from inscriptis import get_text

url = "https://www.wsb.pl/torun/studia-i-szkolenia/studia-podyplomowe/kierunki/tester-oprogramowania-dla-aplikacji-mobilnych-i-serwerowych/program-studiow"
html = urllib.request.urlopen(url).read().decode('utf-8')

text = get_text(html)
print(text)