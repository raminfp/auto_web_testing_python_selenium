## Author : Mostafa Shabani , Github : @smostafa64

from selenium import webdriver
import time


def chromewebdriver():
    return webdriver.Chrome("..\\..\\chromedriver\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get("https://google.com/search?q=Hi")
    driver.execute_script("scroll(0,1500)")
    time.sleep(5)


mysite()

