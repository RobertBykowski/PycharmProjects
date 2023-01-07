
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_for_home():
    browser = webdriver.Firefox()
    url = "https://www.diki.pl/"
    browser.get(url)
    word = "home"

    field = browser.find_element(By.CSS_SELECTOR, ".dikiSearchInputField")
    field.click()
    field.send_keys(word)


    submit = browser.find_element(By.CSS_SELECTOR, ".dikiSearchMainPageSubmit")
    submit.click()

    element = browser.find_element(By.CSS_SELECTOR, ".hw")
    text = element.text
    # print(text)
    assert text == word, f"Oczekiwano tekstu 'at home', otrzymano: '{text}'"


    browser.close()
    print("close! ")

test_search_for_home()

