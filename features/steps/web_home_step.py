#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from behave import *
from features.pages.web_home_page import WebHomePage

use_step_matcher("re")


@given("Eu me preparo para acesso a página home pela primeira vez")
def step_impl(context):
    context.webHome_page = WebHomePage(context.driver)
    context.webHome_page.navegar_pagina(context.config.userdata['url'])

@then("Eu estou na página home")
def step_impl(context):
    context.webHome_page.validarPage()

@then("Eu clico em login")
def step_impl(context):
    context.webHome_page.clicar_login()