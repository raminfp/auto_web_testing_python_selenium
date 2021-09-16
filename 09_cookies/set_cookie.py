from selenium import webdriver
from selenium.webdriver import ActionChains
import time

url = "https://python.org"


def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get(url)

    my_cookie = {'name': 'selenium', 'value': 'this is a test', 'secure': True}
    driver.add_cookie(my_cookie)
    list_of_cookies = driver.get_cookies()
    print(len(driver.get_cookies()))
    for item in list_of_cookies:
        driver.delete_cookie(item['name'])
    print(len(driver.get_cookies()))


mysite()