## Author : Mostafa Shabani, Github: @smostafa64

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("..\\..\\chromedriver\\chromedriver.exe")

driver.maximize_window()
driver.get("https://sharifict.ir/")
original_window = driver.current_window_handle

classMenu = driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/ul/li[5]/div/div[1]/button')
classMenu.click()
seleniumClass = driver.find_element_by_xpath('//a[@href="https://www.skyroom.online/ch/sharifict.ir/selenium"]')
seleniumClass.click()

wait = WebDriverWait(driver, 5)
wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

time.sleep(3)
usr = driver.find_element_by_id("username")
pss = driver.find_element_by_id("password")
usr.send_keys("myUser")
pss.send_keys("myPassword")
driver.find_element_by_xpath('//*[@id="btn_login"]').click()

