from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_download_format(driver):
    driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
    # driver.implicitly_wait(5)
    enabled_button = driver.find_element(By.LINK_TEXT, "Enabled")
    enabled_button.click()
    # downloads_button = driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > a")
    downloads_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Downloads")
    downloads_button.click()
    # pdf_button = driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > a")
    pdf_button = driver.find_element(By.LINK_TEXT, "PDF")
    pdf_button.click()
    # sleep(3)

def test_close_window(driver):
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    # sleep(2)
    # driver.implicitly_wait(2)
    wait = WebDriverWait(driver, 5)
    # close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
    # close_button.click()
    # assert not close_button.is_displayed()

    wait = WebDriverWait(driver, 5)
    close_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, ".modal-footer > p")))
    close_button.click()
    # assert not close_button.is_displayed()
