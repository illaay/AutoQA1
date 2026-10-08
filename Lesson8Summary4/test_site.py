from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    # options = webdriver.Chrome()
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_payment(driver):
    driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
    # driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 5)  # Ожидание до 5 секунд
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Enabled"))).click()
    # link_1.click()
    link_2 = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Downloads")))
    link_2.click()
    link_3 = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "PDF")))
    link_3.click()
    # link_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Enabled")
    # link_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Downloads")
    # link_2 = driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > a")
    # link_3 = driver.find_element(By.PARTIAL_LINK_TEXT, "PDF")
    # link_3 = driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > a")
    sleep(3)
