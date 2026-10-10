import pytest
from selenium import webdriver
from ..pages.login_page import LoginPage


@pytest.fixture(scope="class")
def driver():
    options = webdriver.ChromeOptions()
    # чтобы не мешали алерты
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login_page(driver):
    return LoginPage(driver)
