from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://www.geeksforgeeks.org/")
# element = driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul[1]/li[2]/span")
driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")


actions = ActionChains(driver)
actions.context_click(search_bar).perform()

time.sleep(10)

driver.quit()