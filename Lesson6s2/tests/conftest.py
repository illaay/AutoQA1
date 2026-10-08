import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Lesson6s2.pages.contact_page import ContactPage
from Lesson6s2.pages.auth_page import AuthPage


@pytest.fixture(scope="function")
def driver():
    """Initializes browser instance for each test."""
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def contact_page(driver):
    """Provides an instance of ContactPage."""
    return ContactPage(driver)


@pytest.fixture(scope="function")
def auth_page(driver):
    """Provides an instance of AuthPage."""
    return AuthPage(driver)