from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.amazon.com.br/Quest-modelo-128gb-cor-branca/dp/B0CJZPJLC6/ref=asc_df_B0CJZPJLC6/?tag=googleshopp00-20&linkCode=df0&hvadid=647401608645&hvpos=&hvnetw=g&hvrand=14862999228924962793&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001729&hvtargid=pla-2247148235978&psc=1&mcid=f16329f909383fe2aa4dc057cfd7e895')

result = driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]').text

print (result)
