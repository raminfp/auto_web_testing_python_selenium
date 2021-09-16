from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")
driver.get("http://jqueryui.com/droppable/")
sleep(2)

driver.switch_to.frame(0)

source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

sleep(3)

driver.quit()