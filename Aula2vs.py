from selenium import webdriver    
from selenium.webdriver.common.by import By
import time

nav = webdriver.Chrome()
nav.get('https://www.pichau.com.br/account')
time.sleep(1)

user=nav.find_element(By.ID,'username')

user.send_keys('gustavosantosmudo@gmail.com')

senha = nav.find_element(By.ID,'password')
senha.send_keys('Gu123456789*')
time.sleep(1)
nav.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div/div/div[1]/div/form/button').click()

time.sleep(30)