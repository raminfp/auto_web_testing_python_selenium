import time
from selenium import webdriver

driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")
# driver.get("file:///C:/Users/raminfp/PycharmProjects/web_auto_selenium/01_selenium_elements/selectors_elements.html")
# input_username = driver.find_element_by_name('username')
# input_username = driver.find_element_by_class_name("usrname")
# input_username = driver.find_element_by_css_selector("#loginform > input.usrname")
# input_username = driver.find_element_by_xpath('//*[@id="loginform"]/input[1]')
# input_passwd = driver.find_element_by_id("pass")
# submit_btn = driver.find_element_by_xpath('//*[@id="loginform"]/input[3]')
# input_username.send_keys("hello all")
# input_passwd.send_keys("123456")
# time.sleep(5)
# submit_btn.click()
# print(driver.page_source)
# print(driver.current_url)
# driver.close()
################################################ Tag Name

# driver.get("file:///C:/Users/raminfp/Desktop/Day_1/-Automating-Web-Testing-with-Selenium-and-Python-master/01/22.html")
# find_with_tag = driver.find_element_by_tag_name("h1")
# print(find_with_tag.text)

################################################# Check box
# from selenium.webdriver.common.alert import Alert
# driver.get("file:///C:/Users/raminfp/Desktop/Day_1/-Automating-Web-Testing-with-Selenium-and-Python-master/01/23.html")
# check_box = driver.find_element_by_css_selector("body > form:nth-child(1) > input[type=checkbox]:nth-child(1)")
# check_box.click()
# btn_click = driver.find_element_by_xpath("/html/body/button[1]")
# btn_click.click()
# time.sleep(5)
# Alert(driver).accept()
#################################################



# driver.close()