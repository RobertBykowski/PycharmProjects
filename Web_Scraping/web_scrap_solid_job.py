from requests_html import HTMLSession
session = HTMLSession()

# def get_ofert_links(page):

links = []
url = f"https://www.pracuj.pl/praca/torun;wp/ostatnich%2024h;p,1?rd=0&pn=2"
page = session.get(url)
oferts = page.html.find("li.results__list-container-item a")
# oferts = page.html.find("ul.results__list-container a")
for item in oferts:
    links.append(item.find("a", first=True).attrs["href"])
    # return links

for i in links:
    print(i)
print(len(links))




# def parse_ofert(url):
#     r = session.get(url)
#     title = r.html.find("h1.offer-viewkHIhn3", first=True).text.strip()
#     name_company = r.html.find("h2.offer-viewwtdXJ4", first=True).text.strip().replace("O firmie","")
#     ofert = {
#         "title" : title,
#         "name" : name_company
#     }
#     return ofert
#
# print(parse_ofert(2))






