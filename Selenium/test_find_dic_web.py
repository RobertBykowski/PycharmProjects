# Test sprawdzający poprwność wyszukiwania haseł w słowniku https://www.diki.pl/

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_for_word():

    # create an instance of the Firefox web browser
    browser = webdriver.Firefox()
    # set the URL of the website to be tested
    url = "https://www.diki.pl/"
    # navigate to the website
    browser.get(url)
    # set the word to be searched for on the website https://www.diki.pl/
    word = "home"

    # find the search field element using its CSS selector
    field = browser.find_element(By.CSS_SELECTOR, ".dikiSearchInputField")

    # click on the search field element to focus on it
    field.click()

    # type the word to be searched in the search field
    field.send_keys(word)

    # find the search button element using its CSS selector
    submit = browser.find_element(By.CSS_SELECTOR, ".dikiSearchMainPageSubmit")
    # click on the search button to submit the search
    submit.click()
    # find the element containing the search result using its CSS selector
    element = browser.find_element(By.CSS_SELECTOR, ".hw")
    text = element.text
    # assert that the retrieved text is equal to the searched word
    assert text == word, f"Expected text 'home', got: '{text}'"

    # close the web browser
    browser.close()

# execute the test function

test_search_for_word()

