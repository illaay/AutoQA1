import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_page_screenshot(firefox_driver):
    firefox_driver.get("https://itcareerhub.de/ru")
    payment_methods = firefox_driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_methods.click()
    firefox_driver.save_screenshot("./firefox_screenshot.png")
