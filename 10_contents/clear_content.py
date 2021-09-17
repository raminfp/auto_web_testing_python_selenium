from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://google.com"


def chromewebdriver():
    return webdriver.Chrome("..\\chromedriver\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get(url)

    search_input_box = driver.find_element(By.NAME, 'q')
    search_input_box.send_keys("Hello")
    time.sleep(5)

    search_input_box.clear()

    time.sleep(3)
    driver.close()


mysite()
