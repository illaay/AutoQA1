import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_task_1(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://uitestingplayground.com/textinput')

    text_input = wait.until(EC.visibility_of_element_located((By.ID, 'newButtonName')))
    text_input.clear()
    text_input.send_keys('ITCH')

    button = wait.until(EC.element_to_be_clickable((By.ID, 'updatingButton')))
    button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'ITCH'))
    assert driver.find_element(By.ID, 'updatingButton').text == 'ITCH'


def test_task_2(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    wait.until(EC.text_to_be_present_in_element((By.ID, 'text'), 'Done!'))

    award_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[alt="award"]')))
    assert award_image.get_attribute('alt') == 'award'