from selenium import webdriver
driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")
driver.get("file:///C:/Users/raminfp/PycharmProjects/web_auto_selenium/01_selenium_elements/link_text_selector.html")

get_text = driver.find_element_by_link_text('Google')
print(get_text.text)
