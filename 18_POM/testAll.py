import unittest
from selenium import webdriver
from page import HomePage
from page import AboutPage
from locators import CommonPageLocators
from locators import AboutPageLocator
from messages import *

class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome("..\\chromedriver\chromedriver.exe", options=chrome_options)

    def tearDown(self):
        self.driver.close()


class TestHome(TestPythonOrg):
    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    @unittest.skip
    def test_TC001_python_docs_button(self):
        self.home.mouse_hover(CommonPageLocators.DOC)
        self.home.assert_elem_text(CommonPageLocators.DOC_BTN, "Python Docs")
        self.home.click(CommonPageLocators.DOC_BTN)

    # @unittest.skip
    def test_TC0002_search_python_org(self):

        text_1 = "No results found."
        self.home.search_text(SEARCH_MSG)
        result_py = self.home.elem_result_text(CommonPageLocators.SEARCH_RESULT)
        self.home.assert_compare_text(text_1, result_py)


class TestAbout(TestPythonOrg):

    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    def test_TC003_about_page(self):
        # about_page_message = self.about.elem_result_text(AboutPageLocator.ARTICLE_SECTION)
        # print(about_page_message)
        #
        # self.about.assert_compare_text(about_page_message, ARTICLE_SECTION_MESSAGE)
        self.about.assert_elem_text(AboutPageLocator.ARTICLE_SECTION, ARTICLE_SECTION_MESSAGE)

if __name__ == "__main__":
    unittest.main()