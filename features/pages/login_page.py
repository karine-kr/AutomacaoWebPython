from selenium.webdriver.common.by import By

class LoginPage:
   URL = "https://www.saucedemo.com/"
   def __init__(self, driver):
       self.driver = driver
   def acessar(self):
       self.driver.get(self.URL)
   def preencher_usuario(self, usuario: str):
       self.driver.find_element(By.ID, "user-name").send_keys(usuario)
   def preencher_senha(self, senha: str):
       self.driver.find_element(By.ID, "password").send_keys(senha)
   def clicar_login(self):
       self.driver.find_element(By.ID, "login-button").click()
   def login(self, usuario: str, senha: str):
       self.preencher_usuario(usuario)
       self.preencher_senha(senha)
       self.clicar_login()
   def obter_mensagem_erro(self) -> str:
       return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text