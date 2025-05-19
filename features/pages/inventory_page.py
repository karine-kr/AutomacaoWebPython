from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_product_displayed(self, product_name: str) -> bool:
        """
        Verifica se o produto com nome exato está visível na página.
        """
        product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return any(product.text.strip().lower() == product_name.lower() for product in product_elements)

    def add_product_by_name(self, product_name: str):
        """
        Clica no botão 'Add to cart' do produto com nome especificado.
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if name.lower() == product_name.lower():
                item.find_element(By.TAG_NAME, "button").click()
                break

    def sort_by(self, option_text: str):
        """
        Ordena os produtos usando o select dropdown (ex: 'Price (high to low)').
        """
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_visible_text(option_text)

    def add_most_expensive_items(self, count: int = 2):
        """
        Adiciona os 'count' itens mais caros ao carrinho.
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        products = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            price_text = item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip().replace("$", "")
            price = float(price_text)
            button = item.find_element(By.TAG_NAME, "button")
            products.append((price, button, name))

        products.sort(reverse=True)  # Do mais caro para o mais barato
        for i in range(count):
            products[i][1].click()  # Clica no botão "Add to cart"

    def go_to_cart(self):
        """
        Navega até o carrinho de compras.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
 