from selenium import webdriver
from selenium.webdriver import ActionChains
import time

url = "file:///C:/Users/raminfp/Desktop/Day_1/-Automating-Web-Testing-with-Selenium-and-Python-master/01/iframe_example.html"


def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    iframe = driver.find_element_by_id("#iframe_container > iframe")
    driver.switch_to.frame(iframe)

    time.sleep(5)
    var = driver.find_element_by_xpath('//*[@id="menu-item-2037"]').text
    # out = driver.find_element_by_css_selector("#page")
    # print(out)
    time.sleep(5)

mysite()