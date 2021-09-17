from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import requests

url = "https://python.org"

def chromewebdriver():
    return webdriver.Chrome("..\\chromedriver\\chromedriver.exe")


def mysite():
    driver = chromewebdriver()
    driver.get(url)
    # text_ip = find.elemetn_sdnakd()
    readfile()
    time.sleep(3)
    driver.close()


def readfile():
    my_req = requests.get("https://raw.githubusercontent.com/fuzzdb-project/fuzzdb/master/attack/ip/localhost.txt")
    if my_req:
        if my_req.status_code == 200:
            print(my_req.text)

while True:
    print("Strating web browser ...")
    mysite()
    time.sleep(5)
    print("Please waiting ...")