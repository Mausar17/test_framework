from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    URL_PATH = "inventory.html"

    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def is_loaded(self):
        return self.URL_PATH in self.current_url

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_item_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def click_cart_icon(self):
        self.click(self.CART_ICON)

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE, timeout= 2):
            return int(self.get_text(self.CART_BADGE))
        return 0

