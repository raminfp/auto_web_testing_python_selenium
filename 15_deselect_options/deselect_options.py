from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("..\\chromedriver_win32\\chromedriver.exe")
driver.get("file:///C:/Users/raminfp/PycharmProjects/web_auto_selenium/html_example/deselect_option.html")

select_element = driver.find_element_by_id("langs")
select_obj = Select(select_element)

# select_obj.select_by_value()
select_obj.select_by_index(3)
select_obj.select_by_index(2)

# select_obj.select_by_visible_text()
time.sleep(10)

# select_obj.deselect_by_index(3)
# select_obj.deselect_all()
select_obj.deselect_by_value("rb")
time.sleep(5)



