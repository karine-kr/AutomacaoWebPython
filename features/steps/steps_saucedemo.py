from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.inventory_page import InventoryPage
from features.pages.cart_page import CartPage
from features.pages.checkout_page import CheckoutPage
from features.pages.overview_page import OverviewPage

@given("que estou na página de login")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('faço login com usuário "{username}" e senha "{password}"')
def step_do_login(context, username, password):
    context.login_page.login(username, password)

@then("devo ver a página de inventário")
def step_verify_inventory(context):
    print("URL atual: ", context.driver.current_url)
    assert "inventory" in context.driver.current_url

@then('devo ver a mensagem de erro "{mensagem}"')
def step_verify_error_message(context, mensagem):
    assert mensagem in context.login_page.get_error_message()

@when("realizo logout")
def step_logout(context):
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()

@then("devo ver a página de login novamente")
def step_verify_back_to_login(context):
    assert "saucedemo.com" in context.driver.current_url and "login" in context.driver.page_source

@when('adiciono os produtos "{produto1}" e "{produto2}" ao carrinho')
def step_add_multiple_products(context, produto1, produto2):
    context.inventory = InventoryPage(context.driver)
    context.inventory.add_product_by_name(produto1)
    context.inventory.add_product_by_name(produto2)
    context.inventory.go_to_cart()

@when('ordeno os itens do mais caro ao mais barato')
def step_sort_by_price_desc(context):
    context.inventory = InventoryPage(context.driver)
    context.inventory.sort_by("Price (high to low)")

@when("adiciono os dois itens mais caros ao carrinho")
def step_add_most_expensive(context):
    context.inventory.add_most_expensive_items()
    context.inventory.go_to_cart()

@when('adiciono o produto "{produto}" ao carrinho')
def step_add_single_product(context, produto):
    context.inventory = InventoryPage(context.driver)
    context.inventory.add_product_by_name(produto)
    context.inventory.go_to_cart()

@when('finalizo a compra com os dados "{first}", "{last}", "{postal}"')
def step_checkout(context, first, last, postal):
    context.cart = CartPage(context.driver)
    context.cart.proceed_to_checkout()
    context.checkout = CheckoutPage(context.driver)
    context.checkout.fill_customer_info(first, last, postal)
    context.overview = OverviewPage(context.driver)
    context.overview.finish_purchase()

@when('tento finalizar a compra com os dados "{first}", "{last}", "{postal}"')
def step_try_checkout_with_error(context, first, last, postal):
    context.cart = CartPage(context.driver)
    context.cart.proceed_to_checkout()
    context.checkout = CheckoutPage(context.driver)
    context.checkout.fill_customer_info(first, last, postal)

@then('devo ver a mensagem "Thank you for your order!"')
def step_verify_thank_you(context):
    context.overview = OverviewPage(context.driver)
    assert "Thank you for your order!" in context.overview.get_thank_you_message()

@then("devo ver uma mensagem de erro na finalização")
def step_verify_checkout_error(context):
    context.overview = OverviewPage(context.driver)
    assert context.overview.has_error_message()
 
 