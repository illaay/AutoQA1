import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://itcareerhub.de/ru')
    yield driver
    driver.quit()

# можно разделить на несколько функций, но решил объединить по смыслу проверки
def test_sections_display(driver):
    wait = WebDriverWait(driver, 10)

    # логотип
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[alt="IT Career Hub"]')))
    assert logo.is_displayed()

    # основные кнопки
    texts = ['Программы', 'Способы оплаты', 'О нас', 'Bildungsgutschein', 'Отзывы', 'Блог']
    for text in texts:
        button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
        assert button.is_displayed()

    # кнопки смены языков
    ru_language_button = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-elem-id="1710152827519"] a')
    ))
    assert ru_language_button.is_displayed()
    de_language_button = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-elem-id="1710153064158"] a')
    ))
    assert de_language_button.is_displayed()

    # кнопка контактов
    about_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'О нас')))
    about_button.click()
    contacts_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Контакты')))
    assert contacts_button.is_displayed()


def test_callback(driver):
    wait = WebDriverWait(driver, 10)

    about_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'О нас')))
    about_button.click()
    contacts_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Контакты')))
    contacts_button.click()

    # так как с нажатием здесь трудности, пара вариантов решения
    # (помимо способа клика меняется немного селектор)
    # вариант с кликом через javascript
    callback_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-elem-id="1754046238620"] .tn-atom__button-content')
    ))
    driver.execute_script("arguments[0].click();", callback_button)

    # вариант с имитацией нажатия на enter вместо имитации клика мышью
    # callback_button = wait.until(EC.element_to_be_clickable(
    #     (By.CSS_SELECTOR, '[data-elem-id="1754046238620"] a')
    # ))
    # callback_button.send_keys(webdriver.Keys.ENTER)

    call_to_action_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[field="tn_text_175871291756015470"]')
    ))
    assert call_to_action_button.text == 'Запишитесь на бесплатную карьерную консультацию'
