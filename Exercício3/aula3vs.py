from selenium.webdriver.common.by import By
from selenium import webdriver
import time

drive = webdriver.Chrome()

#drive.get('https://www.leroymerlin.com.br/cama-arauna-solteiro-100percent-madeira-para-colchao-78cm_1567867715') 
drive.get('https://www.samsung.com/br/computers/samsung-book/galaxy-book3-360-15-6-inch-i7-16gb-512gb-np750qfg-ks1br/buy/')

drive.implicitly_wait(3)

try:

    #avaliacao = drive.find_element(By.CLASS_NAME,'bv_numReviews_text').text
    avaliacao = drive.find_element(By.XPATH,'//*[@id="content"]/div/div/div[4]/div[1]/div[3]/section/div[1]/div/div[2]/a/span/span/strong/span[2]').text
    

except:
    avaliacao = "não avaliado"
time.sleep(15)


print(avaliacao)
