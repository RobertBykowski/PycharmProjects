from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.pracuj.pl/praca/tester%20manualny;kw/ostatnich%2030%20dni;p,30")
soup = BeautifulSoup(page.content, 'lxml')

offer_details = soup.find_all("div", class_="offer__info" or "offer-container")
offer_dates = soup.find_all("div", class_="offer-actions")

for list in offer_details:

    offer_name = list.find("a", class_="offer-details__title-link")
    print(*offer_name)
    offer_company_name = list.find("a", class_="offer-company__name")
    print("---|",*offer_company_name)
# for data_ in offer_dates:
#     offer_date = data_.find("span", class_="offer-actions__date-long")
#     print(*offer_date)




