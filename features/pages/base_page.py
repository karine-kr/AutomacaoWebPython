class BasePage:
   def __init__(self, driver):
       self.driver = driver
   def click(self, by, locator):
       self.driver.find_element(by, locator).click()
   def fill(self, by, locator, text):
       self.driver.find_element(by, locator).send_keys(text)
   def get_text(self, by, locator):
       return self.driver.find_element(by, locator).text
   def is_element_displayed(self, by, locator):
       return self.driver.find_element(by, locator).is_displayed()