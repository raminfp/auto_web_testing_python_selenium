from selenium import webdriver


url = "https://google.com"

def chromewebdriver():
    return webdriver.Chrome("..\\chromedriver\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    driver.save_screenshot("windows_google.png")

mysite()