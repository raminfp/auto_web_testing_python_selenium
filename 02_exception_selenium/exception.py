from selenium import webdriver

driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")
driver.get("file:///C:/Users/raminfp/PycharmProjects/web_auto_selenium/02_exception_selenium/exception.html")
getelement = driver.find_element_by_id("asdasd")
getelement.click()
driver.close()


