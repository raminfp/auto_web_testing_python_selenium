from locators import CommonPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def mouse_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def search_text(self, search_string):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CommonPageLocators.SEARCH_BAR)).send_keys(search_string)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CommonPageLocators.SEARCH_GO_BTN)).click()

    def assert_elem_text(self, by_locator, element_string):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == element_string

    def elem_result_text(self, by_locator):
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return result.text

    def assert_compare_text(self, text_1, text_2):
        assert text_1 == text_2

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.python.org/")


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.python.org/psf/about/")