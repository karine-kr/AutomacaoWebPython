from selenium.webdriver.common.by import By

class CartPage:
   def __init__(self, driver):
       self.driver = driver
   def clicar_checkout(self):
       self.driver.find_element(By.ID, "checkout").click()