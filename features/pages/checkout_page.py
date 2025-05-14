from selenium.webdriver.common.by import By
from .base_page import BasePage
class CheckoutPage(BasePage):
   FIRST_NAME = (By.ID, "first-name")
   LAST_NAME = (By.ID, "last-name")
   POSTAL_CODE = (By.ID, "postal-code")
   CONTINUE_BUTTON = (By.ID, "continue")
   def fill_customer_info(self, first, last, postal):
       self.fill(*self.FIRST_NAME, first)
       self.fill(*self.LAST_NAME, last)
       self.fill(*self.POSTAL_CODE, postal)
       self.click(*self.CONTINUE_BUTTON)