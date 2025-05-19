import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def before_all(context):
    try:
        chromedriver_path = os.path.abspath("drivers/chromedriver.exe")
        service = Service(executable_path=chromedriver_path)
        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--incognito")
        context.driver = webdriver.Chrome(service=service, options=options)
        context.driver.implicitly_wait(10)
        
    except Exception as e:
       print(f"Erro ao iniciar o driver: {e}")
       raise

def after_all(context):
   context.driver.quit()