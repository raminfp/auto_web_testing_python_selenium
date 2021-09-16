from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import json

url = "https://python.org"


def chrome_webdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")


def file_writing(data):
    fp = open("myallcookies.txt", "a")
    fp.write(data + "\n")
    fp.close()


def my_site():
    driver = chrome_webdriver()
    driver.get(url)

    list_of_cookies = driver.get_cookies()
    for item in list_of_cookies:
        file_writing(json.dumps(item))


my_site()
