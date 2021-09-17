from selenium.webdriver.common.by import By


class CommonPageLocators():

    SEARCH_BAR = (By.XPATH, '//*[@id="id-search-field"]')
    SEARCH_GO_BTN = (By.XPATH, '//*[@id="submit"]')
    DOC = (By.ID, 'documentation')
    DOC_BTN = (By.CSS_SELECTOR, '#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a')
    SEARCH_RESULT = (By.CSS_SELECTOR, '#content > div > section > form > ul')


class AboutPageLocator():
    ARTICLE_SECTION = (By.XPATH, '//*[@id="content"]/div/section/article/header/h1')
