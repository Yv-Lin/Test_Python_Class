from selenium import webdriver
import time
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.adidas.com.tw/v2/official/SalePageCategory/0?tagShowMore=true&sortMode=PageView&tags=G3609::K33484'
driver.get(url)

# n=0
# while n< 5:
driver.execute_script('window.scrollTo(0,document.body.scrollHeight-1000)')
time.sleep(3)
    # n += 1

infoAll = driver.find_elements(By.CLASS_NAME,'product-card__vertical__wrapper' )

for info in infoAll:
    title = info.find_element(By.CLASS_NAME,'sc-jgUSZD').text
    price = info.find_element(By.CLASS_NAME, 'sc-hbOKPk').text
    print(f'{title}:{price}')
