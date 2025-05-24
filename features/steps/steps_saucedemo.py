from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given("que estou na página de login")
def step_impl(context):
   context.login_page = LoginPage(context.driver)
   context.login_page.acessar()

@when('faço login com usuário "{usuario}" e senha "{senha}"')
def step_impl(context, usuario, senha):
   context.login_page.login(usuario, senha)
   context.inventory_page = InventoryPage(context.driver)

@then("devo ver a página de inventário")
def step_impl(context):
   assert context.inventory_page.esta_na_pagina()

@then('devo ver a mensagem de erro "{mensagem}"')
def step_impl(context, mensagem):
   assert mensagem in context.login_page.obter_mensagem_erro()

@when("realizo logout")
def step_impl(context):
   context.inventory_page.realizar_logout()

@then("devo ver a página de login novamente")
def step_impl(context):
   assert "saucedemo.com" in context.driver.current_url

@when('adiciono ao carrinho os produtos "{produto1}" e "{produto2}" se estiverem disponíveis')
def step_adiciona_produtos_se_existirem(context, produto1, produto2):
   context.inventory = InventoryPage(context.driver)
   produtos = [produto1, produto2]
   for produto in produtos:
       if context.inventory.produto_disponivel(produto):
           context.inventory.adicionar_produto(produto)
       else:
        assert False, f"Produto não encontrado na página: {produto}"
   context.inventory.acessar_carrinho()

@when('finalizo a compra com os dados "{nome}", "{sobrenome}", "{cep}"')
def step_impl(context, nome, sobrenome, cep):
   context.inventory_page.acessar_carrinho()
   context.cart_page = CartPage(context.driver)
   context.cart_page.clicar_checkout()
   context.checkout_page = CheckoutPage(context.driver)
   context.checkout_page.preencher_dados(nome, sobrenome, cep)
   context.checkout_page.finalizar_compra()

@then('devo ver a mensagem "{mensagem}"')
def step_impl(context, mensagem):
   assert mensagem in context.checkout_page.obter_mensagem_final()

@when("adiciono os dois itens mais caros ao carrinho após ordenar por preço")
def step_impl(context):
   context.inventory_page.ordenar_por_preco_desc()
   context.inventory_page.adicionar_dois_mais_caros()
   context.inventory_page.acessar_carrinho()
   context.cart_page = CartPage(context.driver)

@when('adiciono o produto "{produto}" ao carrinho')
def step_impl(context, produto):
   context.inventory_page.adicionar_produto(produto)
   context.inventory_page.acessar_carrinho()
   context.cart_page = CartPage(context.driver)

@when('tento finalizar a compra com os dados "{nome}", "{sobrenome}", "{cep}"')
def step_impl(context, nome, sobrenome, cep):
   context.cart_page.clicar_checkout()
   context.checkout_page = CheckoutPage(context.driver)
   context.checkout_page.preencher_dados(nome, sobrenome, cep)

@then('devo ver uma mensagem de erro "{mensagem}"')
def step_impl(context, mensagem):
   assert mensagem in context.checkout_page.obter_mensagem_erro()