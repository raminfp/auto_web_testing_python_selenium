# >>> import selenium
# >>> selenium.__version__
# '3.141.0'

### For Chrome
from selenium import webdriver
driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe")
driver.get("https://google.com")

### For FireFox
# from selenium import webdriver
# driver = webdriver.Firefox(executable_path="\\geckodriver.exe")
# driver.get("https://google.com/search?q=hello guys.")
