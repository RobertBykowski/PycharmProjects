from requests_html import HTMLSession
session = HTMLSession()

url = f"https://www.pracuj.pl/praca/torun;wp/ostatnich%2024h;p,1?rd=0&pn=2"
page = session.get(url)

