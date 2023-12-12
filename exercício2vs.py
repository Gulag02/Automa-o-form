#https://professoroscarjr.000webhostapp.com/delivery/index.php

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nav = webdriver.Chrome()
nav.get('https://professoroscarjr.000webhostapp.com/delivery/index.php')
time.sleep(1)
nav.find_element(By.XPATH, '/html/body/div[1]/form/div/input').click()
time.sleep(3)

nome = nav.find_element(By.ID,'fnome')
nome.send_keys('Gustavo Dos Santos Mudo')

time.sleep(1)

email = nav.find_element(By.ID,'email_id')
email.send_keys('gustavomudo@gmail.com')

time.sleep(1)

senha = nav.find_element(By.NAME,'pass')
senha.send_keys('Gu123456789*')

time.sleep(1)

senha2 = nav.find_element(By.NAME,'pass2')
senha2.send_keys('Gu123456789*')

time.sleep(1)

local = nav.find_element(By.ID,'country')
local.send_keys('Brasil')

time.sleep(1)

entrar =  nav.find_element(By.XPATH,'/html/body/div[1]/form/input[5]').click()

time.sleep(1)

email_login = nav.find_element(By.ID,'email')
email_login.send_keys('gustavomudo@gmail.com')

senha_login = nav.find_element(By.ID,'senha_id')
senha_login.send_keys('Gu123456789*')

nav.find_element(By.XPATH, '/html/body/div[1]/form/input[3]').click()
time.sleep(15)