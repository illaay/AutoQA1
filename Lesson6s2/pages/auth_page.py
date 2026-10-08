from selenium.webdriver.common.by import By
from Lesson6s2.pages.base_page import BasePage
from Lesson6s2.constants.urls import URLs


class AuthPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "doLogin")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = URLs.AUTH_PAGE

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)