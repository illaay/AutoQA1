from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    @property
    def current_url(self):
        return self.driver.current_url
