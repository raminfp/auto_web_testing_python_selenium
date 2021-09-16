from selenium import webdriver
from selenium.webdriver import ActionChains
import time

url = "https://www.python.org/"


def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get(url)

    #
    assert driver.current_url == url

    download_element = driver.find_element_by_id("downloads")
    action = ActionChains(driver)

    action.move_to_element(download_element).perform()
    #
    driver.back()

    time.sleep(10)


mysite()