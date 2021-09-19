from selenium import webdriver


opts = webdriver.FirefoxOptions()
opts.headless = True
driver = webdriver.Firefox(options=opts)
driver.get("https://google.com/")
print(driver.title)
