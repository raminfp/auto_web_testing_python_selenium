from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")
driver.get("https://google.com")

# driver.forward()

driver.back()



