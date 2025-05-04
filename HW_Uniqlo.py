import time
import requests
import os
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立 Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["商品名稱", "價格"])

# 開啟網頁
driver = webdriver.Chrome()
driver.get('https://www.uniqlo.com/tw/zh_TW/')

htmlfile = driver.page_source

driver.maximize_window()
time.sleep(5)

# 點搜尋圖示
search_btn = driver.find_element(By.CSS_SELECTOR, 'li.li-search')
search_btn.click()
time.sleep(2)

# 點搜尋輸入欄並輸入關鍵字
search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="請輸入關鍵字"]')
search_input.click()
search_input.send_keys('pokemon')
search_input.send_keys(Keys.ENTER)
time.sleep(3)

#Capture Pic
soup = BeautifulSoup(htmlfile, 'html.parser')
imgs = soup.find_all('picture-img')
print(imgs)
time.sleep(2)
i = 1
for img in imgs:
    # print(img['data-landscape-url'])
    path = img['data-landscape-url']
    name = img['alt']
    source = requests.get(path)
    img_source = source.content
    os.makedirs('images', exist_ok=True)

    with open(f'images/{name}-{i}.jpg', 'wb') as f:
        f.write(img_source)

    i += 1

"""
# 自動捲動頁面，載入所有商品
last_height = driver.execute_script("return document.body.scrollHeight")
for _ in range(5):  # 捲動 5 次
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 捲動完後再抓所有商品
info = driver.find_elements(By.CLASS_NAME,'product-description')

for item in info:
    try:
        title = item.find_element(By.CLASS_NAME, 'ec-font-sub-title').text.strip()
        price = item.find_element(By.CLASS_NAME, 'product-price').text.strip()
        print(f'{title} : {price}')
        ws.append([title, price])
    except Exception as e:
        print(' 略過商品：', e)
        continue
        
# 儲存 Excel
wb.save('uniqlo_pokemon.xlsx')
driver.quit()
print('完成！資料已儲存為 uniqlo_pokemon.xlsx')
"""