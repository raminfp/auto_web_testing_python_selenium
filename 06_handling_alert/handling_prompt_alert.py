from selenium import webdriver
from selenium.webdriver import ActionChains
import time

url = "https://www.google.com/"


def chromewebdriver():
    return webdriver.Chrome("..\\chromedriver\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get(url)
    code_alert = "prompt('whats your name? ');"
    driver.execute_script(code_alert)
    time.sleep(10)
    alert = driver.switch_to.alert
    # alert.dismiss()
    alert.send_keys("My name is ramin")

    alert.accept()

    time.sleep(10)

mysite()