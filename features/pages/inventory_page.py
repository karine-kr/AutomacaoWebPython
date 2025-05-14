from selenium.webdriver.common.by import By

from .base_page import BasePage

class InventoryPage(BasePage):

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def get_product_elements(self):

        return self.driver.find_elements(*self.PRODUCT_NAMES)

    def get_add_buttons(self):

        return self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

    def add_product_by_name(self, product_name):

        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for item in items:

            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text

            if name == product_name:

                item.find_element(By.TAG_NAME, "button").click()

                break

    def sort_by(self, method_text):

        from selenium.webdriver.support.ui import Select

        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_visible_text(method_text)

    def add_most_expensive_items(self, count=2):

        self.sort_by("Price (high to low)")

        buttons = self.get_add_buttons()

        for i in range(count):

            buttons[i].click()

    def go_to_cart(self):

        self.click(*self.CART_ICON)
 