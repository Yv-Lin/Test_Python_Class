from re import search

from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get('https://www.google.com/')
driver.get('https://tw.yahoo.com/?p=us')
# driver.save_screenshot('tmpJpg.jpg')
time.sleep(1)
# search = driver.find_element(By.CLASS_NAME,'gLFyf')
search = driver.find_element(By.ID,'header-search-input')

time.sleep(0.5)
search.send_keys('午')
time.sleep(1)
search.send_keys('餐')
time.sleep(1.5)
search.send_keys(Keys.ENTER)



