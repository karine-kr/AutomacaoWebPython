#language:pt

Funcionalidade: Automação do site SauceDemo
 
 Esquema do Cenário: Login com usuário válido
   Dado que estou na página de login
   Quando faço login com usuário "<username>" e senha "<password>"
   Então devo ver a página de inventário
   Exemplos:
   | username                  | password      |
   | standard_user             | secret_sauce  |
   | performance_glitch_user   | secret_sauce  |

 Cenário: Login com usuário bloqueado (locked_out_user)
   Dado que estou na página de login
   Quando faço login com usuário "locked_out_user" e senha "secret_sauce"
   Então devo ver a mensagem de erro "Epic sadface: Sorry, this user has been locked out."
 Cenário: Login e logout (standard_user)
   Dado que estou na página de login
   Quando faço login com usuário "standard_user" e senha "secret_sauce"
   E realizo logout
   Então devo ver a página de login novamente
 Cenário: Finalizar compra com múltiplos itens (standard_user)
   Dado que estou na página de login
   Quando faço login com usuário "standard_user" e senha "secret_sauce"
   E adiciono os produtos "Sauce Labs Backpack" e "Sauce Labs Bolt T-Shirt" ao carrinho
   E finalizo a compra com os dados "Fulano", "Teste", "12345"
   Então devo ver a mensagem "Thank you for your order!"
 Cenário: Finalizar compra com os dois itens mais caros (standard_user)
   Dado que estou na página de login
   Quando faço login com usuário "standard_user" e senha "secret_sauce"
   E ordeno os itens do mais caro ao mais barato
   E adiciono os dois itens mais caros ao carrinho
   E finalizo a compra com os dados "Fulano", "Teste", "12345"
   Então devo ver a mensagem "Thank you for your order!"
 Cenário: Tentativa de compra com erro (problem_user)
   Dado que estou na página de login
   Quando faço login com usuário "problem_user" e senha "secret_sauce"
   E adiciono o produto "Sauce Labs Backpack" ao carrinho
   E tento finalizar a compra com os dados "Fulano", "Teste", "12345"
   Então devo ver uma mensagem de erro na finalização