from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.python.org/events/"


def setup():

    opts = webdriver.ChromeOptions()
    opts.headless = True
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-gpu")
    # opts.add_argument("window-size=1400,2100")
    driver = webdriver.Chrome("..\\chromedriver\\chromedriver.exe", options=opts)
    driver.get(url)
    bs_paser(driver.page_source)


def bs_paser(html_python):
    out_parser = BeautifulSoup(html_python, 'html.parser')
    my_tag_lst_a = out_parser.find_all('a')
    for item in my_tag_lst_a:
        print(item.text)


if __name__ == "__main__":
    setup()



