from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
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


def test_button_click(driver):
    driver.get('https://suninjuly.github.io/redirect_accept.html')
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert 'Math is real magic!' in driver.find_element(By.ID, 'simple_text').text

# def test_with_tabs(driver):
#     # sleep(3)
#     driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#     driver.execute_script("window.open('https://the-internet.herokuapp.com/javascript_alerts', '_blank');")
#     driver.execute_script("window.open('https://google.com', '_blank');")
#     # Получаем список всех вкладок
#     tabs = driver.window_handles
#     print("Идентификаторы вкладок:", tabs)
#     # Переключаемся на вторую вкладку (Google)
#     sleep(2)
#     driver.switch_to.window(tabs[0])
#     sleep(2)
#     print("Текущая вкладка:", driver.current_window_handle)
#     driver.close()
#     sleep(2)
#     tabs = driver.window_handles
#     driver.switch_to.window(tabs[0])
#     print("Текущая вкладка:", driver.current_window_handle)
#     sleep(2)


def test_sum5_1(driver):
    driver.get('https://crossbrowsertesting.github.io/hover-menu.html')
    elements_to_hover = driver.find_element(By.LINK_TEXT, 'Dropdown')
    actions = ActionChains(driver)
    actions.move_to_element(elements_to_hover).perform()

    elements_to_hover2 = driver.find_element(By.LINK_TEXT, 'Secondary Menu')
    actions.move_to_element(elements_to_hover2).perform()

    driver.find_element(By.LINK_TEXT, 'Secondary Action').click()

    assert 'Secondary Page' in driver.find_element(By.CSS_SELECTOR, '.secondary-clicked h1').text


def test_drag_and_drop(driver):
    driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')
    drag = driver.find_element(By.ID, 'draggable')
    drop = driver.find_element(By.ID, 'droppable')
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    assert 'Dropped!' in drop.find_element(By.TAG_NAME, 'p').text


def test_fill_form(driver):
    driver.get('http://suninjuly.github.io/file_input.html')
    fst=driver.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    lst=driver.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    mail=driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    file=driver.find_element(By.CSS_SELECTOR, '[name="file"]')
    submit=driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

    fst.send_keys('Vasya')
    lst.send_keys('Pupkin')
    mail.send_keys('admin@admin.com')
    file_path = r"C:\Users\VN\Downloads\images.jpg"  # Укажите путь к файлу на своем компьютере
    file.send_keys(file_path)
    submit.click()
    #alert = driver.switch_to.alert
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    text = alert.text
    assert 'Congrats, you\'ve passed the task!' in text


# def test_cookies(driver):
#     driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
#     driver.implicitly_wait(5)
#     sleep(3)
#     # driver.delete_all_cookies()
#     driver.add_cookie({
#         "name": "FCCDCF",
#         "value": “VALUE”,
#         "domain": ".globalsqa.com",
#         "path": "/"
#     })
#     driver.refresh()
#     sleep(3)