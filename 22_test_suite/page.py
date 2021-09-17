from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_text(self, by_locator, msg):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(msg)

    def assert_elem_text(self, by_locator, element_string):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == element_string

    def mouse_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.default_username = "Admin"
        self.default_password = "admin123"

    def login(self):
        self.send_text(LoginPageLocators.USERNAME, self.default_username)
        self.send_text(LoginPageLocators.PASSWORD, self.default_password)
        self.click(LoginPageLocators.LOGIN_BTN)
