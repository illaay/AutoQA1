from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _TOTAL_PRICE_LABEL = (By.CLASS_NAME, "summary_total_label")

    def click_checkout(self):
        self.click_element(self._CHECKOUT_BUTTON)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_element(self._FIRST_NAME).send_keys(first_name)
        self.wait_for_element(self._LAST_NAME).send_keys(last_name)
        self.wait_for_element(self._POSTAL_CODE).send_keys(postal_code)
        self.click_element(self._CONTINUE_BUTTON)

    def get_total_price(self):
        return self.get_text(self._TOTAL_PRICE_LABEL)
