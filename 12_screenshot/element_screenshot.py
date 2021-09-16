from selenium import webdriver

url = "https://google.com"

def chromewebdriver():
    return webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")

def mysite():
    driver = chromewebdriver()
    driver.get(url)

    screen = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.LLD4me.yr19Zb.LS8OJ > div > img")
    screen.screenshot("google.png")

mysite()