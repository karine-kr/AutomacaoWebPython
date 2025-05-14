from selenium.webdriver.common.by import By
from .base_page import BasePage
class LoginPage(BasePage):
   URL = "https://www.saucedemo.com/"
   USERNAME = (By.ID, "user-name")
   PASSWORD = (By.ID, "password")
   LOGIN_BUTTON = (By.ID, "login-button")
   ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
   def load(self):
       self.driver.get(self.URL)
   def login(self, username, password):
       self.fill(*self.USERNAME, username)
       self.fill(*self.PASSWORD, password)
       self.click(*self.LOGIN_BUTTON)
   def get_error_message(self):
       return self.get_text(*self.ERROR_MESSAGE)