from selenium import webdriver
from selenium.webdriver import ActionChains
import time

url = "https://www.python.org/"


def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get(url)

    download_element = driver.find_element_by_css_selector("#documentation") #.find_element_by_id("downloads")
    action = ActionChains(driver)
    action.move_to_element(download_element).pause(2)
    action.move_by_offset(xoffset=-1, yoffset=-10).perform()

    time.sleep(20)

mysite()