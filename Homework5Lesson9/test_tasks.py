import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_task1(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/iframes.html')
    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'my-iframe')))

    text_element = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#content > p:nth-child(2)')  # "#content p:nth-of-type(2)"
    ))

    assert 'semper posuere integer et senectus justo curabitur.' in text_element.text


def test_task2(driver):
    driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))

    # можно '#gallery > li:nth-child(1)' (короче), но так точнее
    first_photo_selector = '[class="ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle"]'

    first_photo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, first_photo_selector)))
    trash = wait.until(EC.visibility_of_element_located((By.ID, 'trash')))

    # приходится делать скролл, так как рекламный баннер иногда бывает слишком большим
    # и у меня перекрывает центр trash, из-за чего не может нормально произойти перемещение фото
    gallery = wait.until(EC.presence_of_element_located((By.ID, "gallery")))
    driver.execute_script("arguments[0].scrollIntoView(true);", gallery)

    actions.drag_and_drop(first_photo, trash).perform()

    # можно просто '#galery li', но так проверяем, что переместилась именно первая фотография
    first_photo_in_trash = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, f'#trash li{first_photo_selector}')
    ))
    assert first_photo_in_trash

    photos_in_gallery = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, '#gallery li')
    ))
    # вариант со условием в until() мог бы пригодиться,
    # если бы первое фото не успевало удаляться из DOM-дерева после перемещения
    # и в photos_in_gallery попадало 4 фотографии
    # wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3)
    assert len(photos_in_gallery) == 3
