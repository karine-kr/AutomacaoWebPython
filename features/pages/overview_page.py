from selenium.webdriver.common.by import By
from .base_page import BasePage
class OverviewPage(BasePage):
   FINISH_BUTTON = (By.ID, "finish")
   ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
   THANK_YOU_MESSAGE = (By.CLASS_NAME, "complete-header")
   def finish_purchase(self):
       self.click(*self.FINISH_BUTTON)
   def get_thank_you_message(self):
       return self.get_text(*self.THANK_YOU_MESSAGE)
   def has_error_message(self):
       return self.is_element_displayed(*self.ERROR_MESSAGE)