import time
from typing import KeysView
import pandas as pd
import requests
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立 Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["商品名稱", "價格"])

url ='https://www.uniqlo.com/tw/zh_TW/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(5)
# info = driver.find_element(By.LINK_TEXT,'WOMEN')
# info = driver.find_elements(By.CSS_SELECTOR,'.li-search')

# 找到包含 icon-search 的按鈕父層（通常是 <li class="li-search"> 或其父元素）
search_btn = driver.find_element(By.CSS_SELECTOR, 'li.li-search')
search_btn.click()
time.sleep(2)

# search_icon = driver.find_element(By.CLASS_NAME, 'icon-search')
# search_icon.click()

# 2. 找到輸入欄（含 placeholder）並點擊 focus
search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="請輸入關鍵字"]')
search_input.click()
time.sleep(1)

# 輸入要搜尋的字
search_input.send_keys('pokemon')
search_input.send_keys(Keys.ENTER)
time.sleep(2)
info = driver.find_elements(By.CLASS_NAME,'product-description')

time.sleep(3)

# 自動捲動頁面讓所有商品載入
last_height = driver.execute_script("return document.body.scrollHeight")
n = 0
for item in info:
    time.sleep(2)  # 等待新內容載入
    while n < 3:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1000)')
        time.sleep(1)
        n += 1


        title = item.find_element(By.CLASS_NAME, 'ec-font-sub-title').text
        price = item.find_element(By.CLASS_NAME, 'product-price').text
        # print(f'{title}:{price}')
        print(title)







