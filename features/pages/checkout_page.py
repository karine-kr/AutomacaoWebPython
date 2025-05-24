from selenium.webdriver.common.by import By

class CheckoutPage:
   def __init__(self, driver):
       self.driver = driver
   
   def preencher_dados(self, nome: str, sobrenome: str, cep: str):
       self.driver.find_element(By.ID, "first-name").send_keys(nome)
       self.driver.find_element(By.ID, "last-name").send_keys(sobrenome)
       self.driver.find_element(By.ID, "postal-code").send_keys(cep)
       self.driver.find_element(By.ID, "continue").click()
   
   def finalizar_compra(self):
       self.driver.find_element(By.ID, "finish").click()
   
   def obter_mensagem_final(self) -> str:
       return self.driver.find_element(By.CLASS_NAME, "complete-header").text
   
   def obter_mensagem_erro(self) -> str:
       return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text