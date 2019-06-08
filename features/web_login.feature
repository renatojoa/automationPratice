  @runLogin
  Feature: Teste na funcionalidade de login
    @runLoginDone
    Scenario Outline: Efetuar Login com sucesso
      Given Eu me preparo para acesso a página home pela primeira vez
      Then Eu estou na página home
      Then Eu clico em login
      Given Eu me preparo para acesso a página de autentication
      Then Eu estou na página autentication
      Then Eu informo no campo Email: <email>
      Then Eu inicio a criacao da conta
      Then Eu seleciono o genero Masculino
      Then Eu insiro no campo Nome: <nome>
      Then Eu insiro no campo Sobrenome: <sobrenome>
      Then Eu valido no campo Email: <email>
      Then Eu insiro no campo Password: <password>
      Then Eu insiro nas datas o DD/MM/AA: <dia> / <mes> / <ano>

      Examples: login
        | nome   | sobrenome | email                 | password   | dia | mes       | ano  |
        | Renato | Araujo    | renatojoas@emails.com | oipopo     | 6   | September | 1986 |