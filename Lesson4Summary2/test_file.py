from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
# import os


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    user_name = driver.find_element(By.CSS_SELECTOR, "#username")
    user_name.send_keys("davit")

    user_password = driver.find_element(By.CSS_SELECTOR, "#password")
    user_password.send_keys("davit")

    sleep(5)
