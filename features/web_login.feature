  @runLogin
  Feature: Teste na funcionalidade de login
    Scenario Outline: Efetuar Login com sucesso
      Given Eu me preparo para acesso a página home pela primeira vez
      Then Eu estou na página home
      Then Eu clico em login
      Given Eu me preparo para acesso a página de autentication
      Then Eu estou na página autentication
      Then Eu informo no Campo Email de Login: <email>
      Then Eu informo no Campo Senha de Login: <password>
      Then Eu clico em login para entrar

      Examples: login
        | email                 | password   |
        | renatojoas@email2.com | oipopo     |