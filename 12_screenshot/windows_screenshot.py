from selenium import webdriver


url = "https://google.com"

def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    driver.save_screenshot("windows_google.png")

mysite()