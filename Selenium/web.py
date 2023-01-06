# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://allegro.pl/")

# get element
element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div/div[2]/button[1]")
element.click()
# print complete element
# print(element)
