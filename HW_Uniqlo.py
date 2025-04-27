from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.uniqlo.com/tw/zh_TW/ut.html'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(5)
# info = driver.find_element(By.LINK_TEXT,'WOMEN')
# info = driver.find_elements(By.CSS_SELECTOR,'.li-search')
time.sleep(2)
# aainfo = driver.find_elements(By.CLASS_NAME,'search-box')\
search = driver.find_element(By.CLASS_NAME,'search-box')

search.send_keys('mickey')
# search.click()

"""
# link2 = driver.find_element(By.CLASS_NAME,'h-footer')
# link2.click()
# 點圖片
# img = driver.find_element(By.XPATH, '//img[contains(@src, "w_ut_1280x230.jpg")]')
# img.click()
"""


time.sleep(3)

# for item in info:
#     title = item.find_element(By.CLASS_NAME,'product-card__title').text
#     price = item.find_element(By.CLASS_NAME,'product-card__price').text
#     print(f'{title}:{price}')
#
# time.sleep(5)



