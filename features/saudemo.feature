Feature: Automação do site SauceDemo
 
 Scenario: Login com usuário válido (standard_user)
   Given que estou na página de login
   When faço login com usuário "standard_user" e senha "secret_sauce"
   Then devo ver a página de inventário
 Scenario: Login com usuário válido (performance_glitch_user)
   Given que estou na página de login
   When faço login com usuário "performance_glitch_user" e senha "secret_sauce"
   Then devo ver a página de inventário
 Scenario: Login com usuário bloqueado (locked_out_user)
   Given que estou na página de login
   When faço login com usuário "locked_out_user" e senha "secret_sauce"
   Then devo ver a mensagem de erro "Epic sadface: Sorry, this user has been locked out."
 Scenario: Login e logout (standard_user)
   Given que estou na página de login
   When faço login com usuário "standard_user" e senha "secret_sauce"
   And realizo logout
   Then devo ver a página de login novamente
 Scenario: Finalizar compra com múltiplos itens (standard_user)
   Given que estou na página de login
   When faço login com usuário "standard_user" e senha "secret_sauce"
   And adiciono os produtos "Sauce Labs Backpack" e "Sauce Labs Bolt T-Shirt" ao carrinho
   And finalizo a compra com os dados "Fulano", "Teste", "12345"
   Then devo ver a mensagem "Thank you for your order!"
 Scenario: Finalizar compra com os dois itens mais caros (standard_user)
   Given que estou na página de login
   When faço login com usuário "standard_user" e senha "secret_sauce"
   And ordeno os itens do mais caro ao mais barato
   And adiciono os dois itens mais caros ao carrinho
   And finalizo a compra com os dados "Fulano", "Teste", "12345"
   Then devo ver a mensagem "Thank you for your order!"
 Scenario: Tentativa de compra com erro (problem_user)
   Given que estou na página de login
   When faço login com usuário "problem_user" e senha "secret_sauce"
   And adiciono o produto "Sauce Labs Backpack" ao carrinho
   And tento finalizar a compra com os dados "Fulano", "Teste", "12345"
   Then devo ver uma mensagem de erro na finalização