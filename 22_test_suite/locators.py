from selenium.webdriver.common.by import By


class CommonPageLocators:
    ADMIN = (By.ID, "menu_admin_viewAdminModule")


class LoginPageLocators:

    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BTN = (By.ID, "btnLogin")
    SPAN_MSG = (By.ID, "spanMessage")
    WELCOME_DASHBOARD = (By.XPATH, '//*[@id="welcome"]')


class AdminPageLocators:

    JOB = (By.ID, "menu_admin_Job")
    JOB_TITLE = (By.ID, "menu_admin_viewJobTitleList")
    JOB_TITLE_ADD_BTN = (By.ID, "btnAdd")
    JOB_JOB_TITLE_NAME = (By.ID, "jobTitle_jobTitle")
    JOB_JOB_TITLE_DESC = (By.ID, "jobTitle_jobDescription")
    JOB_TITLE_SAVE = (By.ID, "btnSave")


class WorkShiftPageLocators:
    JOB = (By.ID, "menu_admin_Job")
    ADMIN_WORK_SHIFT = (By.ID, "menu_admin_workShift")
    ADMIN_WORK_SHIFT_ADD_BTN = (By.ID, "btnAdd")
    WORK_SHIFT_NAME = (By.ID, "workShift_name")
    WORK_SHIFT_SAVE = (By.ID, "btnSave")
