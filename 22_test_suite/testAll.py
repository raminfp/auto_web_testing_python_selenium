import time
import unittest
from selenium import webdriver
from page import LoginPage
from locators import CommonPageLocators
from locators import AdminPageLocators
from locators import LoginPageLocators
from locators import WorkShiftPageLocators
import string
import random


class TestHRMBase(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome("..\\chromedriver\chromedriver.exe", options=chrome_options)

    def tearDown(self):
        self.driver.close()


class TestLogin(TestHRMBase):
    def setUp(self):
        super().setUp()
        self.login = LoginPage(self.driver)

    @unittest.skip
    def test_TC_L_001(self):
        self.login.send_text(LoginPageLocators.USERNAME, self.login.default_username)
        self.login.send_text(LoginPageLocators.PASSWORD, self.login.default_password)
        self.login.click(LoginPageLocators.LOGIN_BTN)
        self.login.assert_elem_text(LoginPageLocators.WELCOME_DASHBOARD, "Welcome Paul")

    @unittest.skip
    def test_TC_L_002(self):
        self.login.send_text(LoginPageLocators.USERNAME, self.login.default_username)
        self.login.send_text(LoginPageLocators.PASSWORD, "ihjhjkhkjhkk")
        self.login.click(LoginPageLocators.LOGIN_BTN)
        self.login.assert_elem_text(LoginPageLocators.SPAN_MSG, "Invalid credentials")


class TestAdmin(TestHRMBase):

    def setUp(self):
       super().setUp()
       self.admin = LoginPage(self.driver)
       self.admin.login()

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @unittest.skip
    def test_TC_A_001(self):
        job_title = self.id_generator()
        job_desc = self.id_generator()
        self.admin.mouse_hover(CommonPageLocators.ADMIN)
        self.admin.mouse_hover(AdminPageLocators.JOB)
        self.admin.click(AdminPageLocators.JOB_TITLE)
        self.admin.click(AdminPageLocators.JOB_TITLE_ADD_BTN)
        self.admin.send_text(AdminPageLocators.JOB_JOB_TITLE_NAME, job_title)
        self.admin.send_text(AdminPageLocators.JOB_JOB_TITLE_DESC, job_desc)
        self.admin.click(AdminPageLocators.JOB_TITLE_SAVE)


class TestWorkShift(TestHRMBase):

    def setUp(self):
        super().setUp()
        self.workshift = LoginPage(self.driver)
        self.workshift.login()

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def test_TC_W_003(self):
        self.workshift.mouse_hover(CommonPageLocators.ADMIN)
        self.workshift.mouse_hover(AdminPageLocators.JOB)
        self.workshift.click(WorkShiftPageLocators.ADMIN_WORK_SHIFT)
        self.workshift.click(WorkShiftPageLocators.ADMIN_WORK_SHIFT_ADD_BTN)
        self.workshift.send_text(WorkShiftPageLocators.WORK_SHIFT_NAME, self.id_generator())
        self.workshift.click(WorkShiftPageLocators.WORK_SHIFT_SAVE)


if __name__ == "__main__":
    unittest.main()
