# >>> import selenium
# >>> selenium.__version__
# '3.141.0'

### For Chrome
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\raminfp\\Desktop\\Day_1\\chromedriver_win32\\chromedriver.exe")
driver.get("https://google.com")

### For FireFox
# from selenium import webdriver
# driver = webdriver.Firefox(executable_path="C:\\Users\\raminfp\\Desktop\\Day_1\\test\\geckodriver.exe")
# driver.get("https://google.com/search?q=hello guys.")
