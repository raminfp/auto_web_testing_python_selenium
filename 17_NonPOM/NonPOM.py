import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestPythonOrg(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome("..\\chromedriver\chromedriver.exe", options=chrome_options)

    @unittest.skip
    def test_TC001_python_docs_button(self):
        self.driver.get("https://www.python.org/")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "documentation")))
        ActionChains(self.driver).move_to_element(element).perform()
        locator = "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a"
        py3btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        assert py3btn.text == "Python Docs"
        # assert py3btn.text == "asdasdsadadad"
        # print(self.driver.page_source)
        py3btn.click()

    @unittest.skip
    def test_TC0002_search_python_org(self):
        self.driver.get("https://www.python.org/")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id-search-field"]'))).send_keys("asdsa")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit"]'))).click()
        result_not_found = self.driver.find_element_by_css_selector("#content > div > section > form > ul")
        assert result_not_found.text == "No results found."

    def test_TC003_about_page(self):
        self.driver.get("https://www.python.org/psf/about/")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/section/article/header/h1')))
        assert element.text == "About the Python Software Foundation"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()