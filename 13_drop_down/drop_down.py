from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")
driver.get("file:///C:/Users/raminfp/PycharmProjects/web_auto_selenium/html_example/24_clickable_dropdown.html")

search_bar = driver.find_element_by_css_selector("body > div > button")
actions = ActionChains(driver)
actions.click(search_bar).perform()
