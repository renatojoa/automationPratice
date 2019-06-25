  @runNewAccount
  Feature: Teste na funcionalidade de login
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
      Then Eu valido no campo Nome: <nome>
      Then Eu valido no campo Sobrenome: <sobrenome>
      Then Eu insiro no campo Endereco: <endereco>
      Then Eu insiro no campo Cidade: <cidade>
      Then Eu insiro no campo Estado: <estado>
      Then Eu insiro no campo Zipcode: <zipcode>
      Then Eu defino no campo Pais: <pais>, Telefone: <telefone> e Futuro endereco
      Then Eu insiro dados no campo Outros
      Then Eu concluo o cadastro

      Examples: login
        | nome   | sobrenome | email                 | password   | dia | mes       | ano  | endereco   | cidade | estado | pais | zipcode | telefone |
        | Renato | Araujo    | renatojoas@email2.com | oipopo     | 6   | September | 1986 | Rua Amabai | Recife | Ohio  | United States | 51020   | 81996873479 |