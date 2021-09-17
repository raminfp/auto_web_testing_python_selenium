from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

url = "file:///C:/Users/raminfp/PycharmProjects/web_auto_selenium/html_example/select_option.html"

def chromewebdriver():
    return webdriver.Chrome("..\\chromedriver\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    select_elements = driver.find_element_by_id("langs")
    select_obj = Select(select_elements)
    # for item in select_obj.options:
        # print(item.text)
    select_obj.select_by_value("py")
    time.sleep(5)

mysite()