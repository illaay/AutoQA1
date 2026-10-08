from selenium.webdriver.common.by import By
from Lesson6s2.pages.base_page import BasePage
from Lesson6s2.constants.urls import URLs


class ContactPage(BasePage):
    # Locators (Kept encapsulated inside the page class)
    NAME_FIELD = (By.ID, "name")
    EMAIL_FIELD = (By.ID, "email")
    PHONE_FIELD = (By.ID, "phone")
    SUBJECT_FIELD = (By.ID, "subject")
    DESCRIPTION_FIELD = (By.ID, "description")
    # SUBMIT_BTN = (By.ID, "submitContact")
    SUBMIT_BTN = (By.CSS_SELECTOR, '#contact [type="button"]')
    LOCATION_INFO = (By.CSS_SELECTOR, ".card-body h4 + p")
    SUCCESSFUL_TEXT = (By.CSS_SELECTOR, "#contact h3")


    def __init__(self, driver):
        super().__init__(driver)
        self.url = URLs.CONTACT_PAGE

    def open(self):
        self.driver.get(self.url)

    def fill_contact_form(self, name, email, phone, subject, message):
        self.type_text(self.NAME_FIELD, name)
        self.type_text(self.EMAIL_FIELD, email)
        self.type_text(self.PHONE_FIELD, phone)
        self.type_text(self.SUBJECT_FIELD, subject)
        self.type_text(self.DESCRIPTION_FIELD, message)

    def submit_form(self):
        # Сначала находим элемент кнопки через встроенный механизм Selenium
        button_element = self.driver.find_element(*self.SUBMIT_BTN)

        # Мгновенно центрируем экран на кнопке с помощью JavaScript (без лагов и рывков)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_element)

        # Это обойдет любые проблемы с масштабированием экрана ноутбука и ошибками перекрытия (ElementClickIntercepted)
        self.driver.execute_script("arguments[0].click();", button_element)

    def get_location_info(self):
        return self.get_text(self.LOCATION_INFO)

    def get_location_text(self):
        return self.get_text(self.LOCATION_INFO)