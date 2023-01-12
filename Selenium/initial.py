

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def search_for_elements():

    # create an instance of the Firefox web browser
    browser = webdriver.Firefox()


    # set the URL of the website to be tested
    url = "https://mavelo.pl/"
    # navigate to the website
    browser.get(url)
    time.sleep(1)


    # find the search field element using its CSS selector
    field = browser.find_element(By.CSS_SELECTOR, "div.promo-item:nth-child(1) > a:nth-child(1)")

    # click on the search field element to focus on it
    field.click()
    time.sleep(1)

    field_1 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")


    # close the web browser
    browser.close()

# execute the test function

search_for_elements()

