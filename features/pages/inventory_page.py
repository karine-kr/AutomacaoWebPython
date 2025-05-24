from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class InventoryPage:
   def __init__(self, driver):
       self.driver = driver

   def esta_na_pagina(self) -> bool:
       return "inventory" in self.driver.current_url
   
   def realizar_logout(self):
       self.driver.find_element(By.ID, "react-burger-menu-btn").click()
       self.driver.find_element(By.ID, "logout_sidebar_link").click()

   def produto_disponivel(self, nome_produto: str) -> bool:
       elementos_nome = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
       return any(produto.text.strip().lower() == nome_produto.lower() for produto in elementos_nome)
   
   def adicionar_produto(self, nome_produto: str):
       items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
       for item in items:
           nome = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
           if nome.lower() == nome_produto.lower():
               item.find_element(By.TAG_NAME, "button").click()
               break          
   
   def ordenar_por_preco_desc(self):
       select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
       select.select_by_value("hilo")
   
   def adicionar_dois_mais_caros(self):
       botoes = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
       for botao in botoes[:2]:
           botao.click()
   
   def acessar_carrinho(self):
       self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()