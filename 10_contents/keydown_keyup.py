from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

url = "https://google.com"

def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    search_input_box = driver.find_element(By.NAME, 'q')
    action = ActionChains(driver)

    action.key_down(Keys.SHIFT)
    time.sleep(5)
    action.send_keys_to_element(search_input_box, "selenium")
    action.key_up(Keys.SHIFT)
    action.key_down(Keys.SPACE)
    action.key_up(Keys.SPACE)
    action.send_keys("webdriver" + Keys.ENTER)
    time.sleep(5)
    action.perform()
    time.sleep(5)

mysite()