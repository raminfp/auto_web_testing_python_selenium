from selenium import webdriver
from selenium.webdriver import ActionChains
import time


url = "https://www.python.org/"


def chromewebdriver():
    return webdriver.Chrome("..\\chromedriver\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    download_element = driver.find_element_by_id("downloads")
    action = ActionChains(driver)

    action.move_to_element(download_element).perform()

    # downlaod = driver.find_element_by_css_selector("#downloads > ul > li.tier-2.super-navigation > div.download-os-windows > p:nth-child(2) > a")
    download = driver.find_element_by_css_selector("#downloads > ul > li.tier-2.element-3")
    download.click()

    time.sleep(20)

mysite()