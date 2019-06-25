#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from behave import *
from features.pages.web_autentication_page import WebAutenticationPage

use_step_matcher("re")

@given("Eu me preparo para acesso a página de autentication")
def step_impl(context):
        context.webAutentication_page = WebAutenticationPage(context.driver)

@given("Eu me preparo para acesso a página de autentication pela primeira vez")
def step_impl(context):
        context.webAutentication_page = WebAutenticationPage(context.driver)
        context.webAutentication_page.navegar_pagina(context.config.userdata['url'])

@step("Eu estou na página autentication")
def step_impl(context):
        context.webAutentication_page.validarPage()

@step("Eu informo no Campo Email de Login: (?P<email>.+)")
def step_impl(context, email):
        context.webAutentication_page.insereEmailLogin(email)

@step("Eu informo no Campo Senha de Login: (?P<senha>.+)")
def step_impl(context, senha):
        context.webAutentication_page.inserePasswordLogin(senha)

@step("Eu clico em login para entrar")
def step_impl(context):
        context.webAutentication_page.realizaLogin()

@step("Eu informo no campo Email: (?P<email>.+)")
def step_impl(context, email):
        context.webAutentication_page.insereEmail(email)

@step("Eu inicio a criacao da conta")
def step_impl(context):
        context.webAutentication_page.clica_inicio_cri()

@step("Eu seleciono o genero Masculino")
def step_impl(context):
        context.webAutentication_page.selecionaSexo()

@step("Eu insiro no campo Nome: (?P<nome>.+)")
def step_impl(context, nome):
        context.webAutentication_page.insereNome(nome)

@step("Eu insiro no campo Sobrenome: (?P<sobrenome>.+)")
def step_impl(context, sobrenome):
        context.webAutentication_page.insereSobrenome(sobrenome)

@step("Eu valido no campo Email: (?P<email>.+)")
def step_impl(context, email):
        context.webAutentication_page.validaEmail(email)

@step("Eu insiro no campo Password: (?P<password>.+)")
def step_impl(context, password):
        context.webAutentication_page.inserePassword(password)

@step("Eu insiro nas datas o DD/MM/AA: (?P<dia>.+) / (?P<mes>.+) / (?P<ano>.+)")
def step_impl(context, dia, mes, ano):
        context.webAutentication_page.defineDataNasc(dia, mes, ano)

@step("Eu valido no campo Nome: (?P<nome>.+)")
def step_impl(context, nome):
        context.webAutentication_page.validaNome(nome)

@step("Eu valido no campo Sobrenome: (?P<sobrenome>.+)")
def step_impl(context, sobrenome):
        context.webAutentication_page.validaSobrenome(sobrenome)

@step("Eu insiro no campo Endereco: (?P<endereco>.+)")
def step_impl(context, endereco):
        context.webAutentication_page.insereEndereco(endereco)

@step("Eu insiro no campo Cidade: (?P<cidade>.+)")
def step_impl(context, cidade):
        context.webAutentication_page.insereCidade(cidade)

@step("Eu insiro no campo Estado: (?P<state>.+)")
def step_impl(context, state):
        context.webAutentication_page.insereEstado(state)

@step("Eu insiro no campo Zipcode: (?P<zipcode>.+)")
def step_impl(context, zipcode):
        context.webAutentication_page.insereZipcode(zipcode)
    
@step("Eu defino no campo Pais: (?P<pais>.+), Telefone: (?P<telefone>.+) e Futuro endereco")
def step_impl(context, pais, telefone):
        context.webAutentication_page.definePais(pais)
        context.webAutentication_page.insereTelefone(telefone)
        context.webAutentication_page.insereAssing()

@step("Eu insiro dados no campo Outros")
def step_impl(context):
        context.webAutentication_page.insereOutros()

@step("Eu concluo o cadastro")
def step_impl(context):
        context.webAutentication_page.confirmaRegistro()
