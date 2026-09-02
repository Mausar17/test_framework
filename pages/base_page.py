from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator, timeout=None):
        try:
            wait_time = timeout or self.DEFAULT_TIMEOUT
            WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def navigate_to(self, url):
        self.driver.get(url)

    @property
    def current_url(self):
        return self.driver.current_url