from selenium.webdriver.common.by import By
from .base_page import BasePage
from .inventory_page import InventoryPage

class LoginPage(BasePage):
    _URL = "https://saucedemo.com"
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.open_url(self._URL)

    def login_as(self, username, password):
        self.wait_for_element(self._USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self._PASSWORD_INPUT).send_keys(password)
        self.click_element(self._LOGIN_BUTTON)
        return InventoryPage(self.driver)
