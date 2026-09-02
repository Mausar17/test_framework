from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.navigate_to(self.URL)
        return self

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def login_expecting_success(self, username, password) -> InventoryPage:
        self.login(username, password)
        return InventoryPage(self.driver)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def has_error_message(self):
        return self.is_visible(self.ERROR_MESSAGE, timeout=3)
