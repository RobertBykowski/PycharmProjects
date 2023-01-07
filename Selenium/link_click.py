from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
url = "https://selenium-python.readthedocs.io/index.html"
browser.get(url)

element = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/ul/li[1]/a")
if element.is_enabled():
    element.click()
    print("was clicked")
else:
    print("Element jest nieaktywny i nie można go kliknąć")

sleep(5)
browser.close()
print("close! ")

