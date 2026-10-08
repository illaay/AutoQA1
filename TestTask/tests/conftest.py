import pytest
from selenium import webdriver
from TestTask.pages.login_page import LoginPage
...
...


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = LoginPage(driver)
    request.cls.success_login = request.cls.driver.success_login("standard_user", "secret_sauce")

    yield request.cls.success_login
    driver.quit()

