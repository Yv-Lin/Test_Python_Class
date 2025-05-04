from selenium import webdriver
import time
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.adidas.com.tw/'
driver.get(url)
driver.maximize_window()

link = driver.find_element(By.CLASS_NAME,'sc-vScKV')

link.click()