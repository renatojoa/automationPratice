#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class WebHomePage(BasePage):
    btnLogin = (By.CLASS_NAME, "login")

    def navegar_pagina(self, url):
        self.open_url(url)

    def validarPage(self):
        time.sleep(3)
        assert self.get_title() == "My Store"

    def clicar_login(self):
        self.click(self.btnLogin)