from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage

class InventoryPage(BasePage):
    _ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    _ADD_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    _ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_target_products_to_cart(self):
        self.click_element(self._ADD_BACKPACK)
        self.click_element(self._ADD_TSHIRT)
        self.click_element(self._ADD_ONESIE)

    def go_to_cart(self):
        self.click_element(self._CART_LINK)
        return CartPage(self.driver)
