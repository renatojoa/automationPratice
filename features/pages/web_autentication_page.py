#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium.webdriver.support.wait import WebDriverWait

from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class WebAutenticationPage(BasePage):
    #MAIN AUTENTICATION PAGE
    lblEmailCreateUser = (By.ID, 'email_create') 
    btnCreateUser = (By.ID, 'SubmitCreate')
    lblEmailLogin = (By.ID, 'email')
    lblPasswordLogin = (By.ID, 'passwd')
    btnLogin = (By.ID, 'SubmitLogin')
    txtError = (By.ID, '//*[@id="center_column"]/div[1]/ol/li')
    txtErrorEmailInvalid = (By.ID, '//*[@id="center_column"]/div[1]/ol/li//*[@id="center_column"]/div[1]/ol/li')
    

    #PERSONAL INFORMATION
    rdioGender = (By.ID, 'uniform-id_gender1')
    lblFirstName = (By.ID, 'customer_firstname')
    lblLastName = (By.ID, 'customer_lastname')
    lblEmail = (By.ID, 'email')
    lblPassword = (By.ID, 'passwd')
    cmbBornDay = (By.ID, 'days')
    cmbBornMonth = (By.ID, 'months')
    cmbBornYear = (By.ID, 'years')
    
    #YOUR ADDRESS
    lblFirstName2 = (By.ID, 'firstname')
    lblLastName2 = (By.ID, 'lastname')
    lblCompany = (By.ID, 'company')
    lblAddress = (By.ID,  'address1')
    lblCity = (By.ID, 'city')
    cmbState = (By.ID, 'id_state')
    lblZipcode = (By.ID, 'postcode')
    cmbCountry = (By.ID, 'id_country')
    lblOther = (By.ID, 'other')
    lblPhone = (By.ID, 'phone_mobile')
    lblAlias = (By.ID, 'alias')
    btnSubmitAcc = (By.ID, 'submitAccount')
    
    #Navigation
    def navegar_pagina(self, url):
        self.open_url(url)

    def validarPage(self):
        print(self.get_title())
        assert self.get_title() == "Login - My Store"

    #Frist Page
    def insereEmailLogin(self, email):
        self.type_in(self.lblEmailLogin, email)

    def inserePasswordLogin(self, password):
        self.type_in(self.lblPasswordLogin, password)
    
    def realizaLogin(self):
        self.click(self.btnLogin)
        time.sleep(3)
        assert self.get_title() == "My account - My Store"

    def insereEmail(self, email):
        self.type_in(self.lblEmailCreateUser, email)

    def clica_inicio_cri(self):
        self.click(self.btnCreateUser)

    #FormPage
    def selecionaSexo(self):
        time.sleep(4)
        self.click(self.rdioGender)

    def insereNome(self, name):
        self.type_in(self.lblFirstName, name)

    def insereSobrenome(self, sobrenome):
        self.type_in(self.lblLastName, sobrenome)

    def validaEmail(self, email):
        assert self.return_value(self.lblEmail) == email

    def validaNome(self, name):
        assert self.return_value(self.lblFirstName2) == name
    
    def validaSobrenome(self, lastname):
        assert self.return_value(self.lblLastName2) == lastname

    def inserePassword(self, password):
        self.type_in(self.lblPassword, password)

    def defineDataNasc(self, bornDay, bornMonth, bornYear):
        self.select_in_combo_by_value2(self.cmbBornDay, bornDay)
        self.select_in_combo_by_index(self.cmbBornMonth, 9)
        self.select_in_combo_by_value2(self.cmbBornYear, bornYear)

    def insereEndereco(self, address):
        self.type_in(self.lblAddress, address)

    def insereCidade(self, city):
        self.type_in(self.lblCity, city)

    def insereEstado(self, state):
        self.select_in_combo_by_index(self.cmbState, 4)
    
    def insereZipcode(self, zipcode):
        self.type_in(self.lblZipcode, zipcode)

    def definePais(self, country):
        self.select_in_combo_by_text(self.cmbCountry, country)

    def insereOutros(self):
        self.type_in(self.lblOther, "Any Value To Procced")
    
    def insereTelefone(self, phone):
        self.type_in(self.lblPhone, phone)

    def insereAssing(self):
        self.type_in(self.lblAlias, "Any Value To Validation")

    def confirmaRegistro(self):
        self.click(self.btnSubmitAcc)
        time.sleep(4)
        assert self.get_title() == "My account - My Store"

    def preenche_dadosPessoais(self, name, lastName, email, password, bornDay, bornMonth, bornYear, 
    endereco, cidade, zipcode, pais, others, telefone):
        self.selecionaSexo()
        self.insereNome(name)
        self.insereSobrenome(lastName)
        self.validaEmail(email)
        self.inserePassword(password)
        self.defineDataNasc(bornDay, bornMonth, bornYear)
        self.insereEndereco(endereco)
        self.insereCidade(cidade)
        self.insereEstado()
        self.insereZipcode(zipcode)
        self.definePais(pais)
        self.insereOutros(others)
        self.insereTelefone(telefone)
        self.insereAssing()
    