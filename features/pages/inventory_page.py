from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
   def __init__(self, driver):
       self.driver = driver
   
   def is_product_displayed(self, product_name: str) -> bool:
       product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
       return any(product.text.strip().lower() == product_name.lower() for product in product_elements)
   
   def add_product_by_name(self, product_name: str):
       items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
       for item in items:
           name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
           if name.lower() == product_name.lower():
               item.find_element(By.TAG_NAME, "button").click()
               break
   
   def sort_by(self, option_text: str):
       dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
       dropdown.select_by_visible_text(option_text)
   
   def add_most_expensive_items(self, count: int = 2):
       items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
       products = []
       for item in items:
           price_text = item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip().replace("$", "")
           try:
               price = float(price_text)
           except ValueError:
               continue 
           button = item.find_element(By.TAG_NAME, "button")
           products.append((price, button))
       products.sort(key=lambda x: x[0], reverse=True)
       for i in range(min(count, len(products))):
           products[i][1].click()
   
   def go_to_cart(self):
       self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()