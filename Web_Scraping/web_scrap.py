from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get("https://www.pracuj.pl/praca/tester%20manualny;kw/ostatnich%2030%20dni;p,30?sc=0")
soup = BeautifulSoup(page.content, 'lxml')

offer_details = soup.find_all("a", class_="offer__click-area")
print(offer_details)

offer_details = soup.find_all("div", class_="offer" or "offer-container")
print(offer_details)

# # offer_dates = soup.find_all("div", class_="offer-actions")
# df1 = []
# df2 = []
# for list in offer_details:
#
#     offer_name = list.find("a", class_="offer-details__title-link").text
#     df1.append(offer_name)
#
#     offer_company_name = list.find("a", class_="offer-company__name").text
#     df2.append(offer_company_name)
# df_all = []
#
# df_all = pd.DataFrame({"Nazwa": df1, "Firma" : df2})
# df_all.index = df_all.index + 1
# df_all.style
# print(df_all)







