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