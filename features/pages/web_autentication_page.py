#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium.webdriver.support.wait import WebDriverWait

from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebAutenticationPage(BasePage):
    lblCreateUser = (By.ID, 'email_create') 
    btnCreateUser = (By.ID, 'SubmitCreate')

    #PERSONAL INFORMATION
    rdioGender = (By.ID, 'uniform-id_gender1')
    lblFirstName = (By.ID, 'customer_firstname')
    lblLastName = (By.ID, 'customer_lastname')
    lblEmail = (By.ID, 'email')
    lblPassword = (By.ID, 'passwd')
    cmbBornDay = (By.NAME, 'days')
    cmbBornMonth = (By.ID, 'months')
    cmbBornYear = (By.ID, 'years')
    
    #YOUR ADDRESS
    lblCompany = (By.ID, 'company')
    lblAddress = (By.ID,  'address1')
    lblCity = (By.ID, 'city')
    cmbState = (By.ID, 'id_state')
    lblZipcode = (By.ID, 'postcode')
    cmbCountry = (By.ID, 'id_country')
    lblPhone = (By.ID, 'phone_mobile')
    lblAlias = (By.ID, 'alias')
    btnSubmitAcc = (By.ID, 'submitAccount')
    

    def navegar_pagina(self, url):
        self.open_url(url)

    def validarPage(self):
        print(self.get_title())
        assert self.get_title() == "Login - My Store"

    def insereEmail(self, email):
        self.type_in(self.lblCreateUser, email)

    def clica_inicio_cri(self):
        self.click(self.btnCreateUser)

    def selecionaSexo(self):
        time.sleep(4)
        self.click(self.rdioGender)

    def insereNome(self, name):
        self.type_in(self.lblFirstName, name)

    def insereSobrenome(self, sobrenome):
        self.type_in(self.lblLastName, sobrenome)

    def validaEmail(self, email):
        assert self.return_value(self.lblEmail) == email

    def inserePassword(self, password):
        self.type_in(self.lblPassword, password)

    def defineDataNasc(self, bornDay, bornMonth, bornYear):
        self.write(self.cmbBornDay, bornDay)
        self.select_in_combo_visible_text(self.cmbBornDay, bornDay)
        self.select_in_combo_by_value(self.cmbBornMonth, bornMonth)
        self.select_in_combo_by_value(self.cmbBornYear, bornYear)

    def preenche_dadosPessoais(self, name, lastName, email, password, bornDay, bornMonth, bornYear):
        self.selecionaSexo()
        self.insereNome(name)
        self.insereSobrenome(lastName)
        self.validaEmail(email)
        self.inserePassword(password)
        self.defineDataNasc(bornDay, bornMonth, bornYear)

    def clicar_forgot(self):
        self.click(self.btnForgot)

    def valida_loginError2(self):
        assert self.return_text(self.lblLoginError2) == '* E-mail ou senha incorretos'