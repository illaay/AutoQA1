import pytest


# @pytest.mark.usefixtures("driver")
class TestSauceDemoOrderFlow:
    inventory_page = None
    cart_page = None

    def test_step1_login(self, login_page):
        login_page.open()
        TestSauceDemoOrderFlow.inventory_page = login_page.login_as("standard_user", "secret_sauce")
        assert "inventory.html" in self.inventory_page.current_url

    def test_step2_add_to_cart_and_checkout(self):
        self.inventory_page.add_target_products_to_cart()
        TestSauceDemoOrderFlow.cart_page = self.inventory_page.go_to_cart()
        self.cart_page.click_checkout()
        assert "checkout-step-one.html" in self.cart_page.current_url

    def test_step3_fill_form_and_verify_total(self):
        self.cart_page.fill_checkout_form("fnjdkvnjdk", "bfjdnkvmlkc", "123456")
        total_text = self.cart_page.get_total_price()
        assert "Total: $58.29" in total_text
