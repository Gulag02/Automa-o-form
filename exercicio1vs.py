from selenium import webdriver
from selenium.webdriver.common.by import By

nav = webdriver.Chrome()

nav.get('https://www.google.com.br/')

""" DIGITAR NA BUSCA """
nav.find.element(By.NAME'q').send_keys('tempo agora')

""" CLICAR PARA BUSCAR """

result = nav.find_element(By.NAME,'btnk').click()

print(result)