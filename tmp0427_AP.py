from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

url = 'https://www.nike.com/tw/'
driver = webdriver.Chrome()
driver.get(url)
htmlfile = driver.page_source
soup = BeautifulSoup(htmlfile,'html.parser')
imgs=soup.find_all('img')
# print(imgs)
i=0
for img in imgs:
    # print(img['data-landscape-url'])
    # 取得HTML img 標籤內資訊
    path = img['data-landscape-url']
    name = img['alt']
    # 取得標籤內URL
    source = requests.get(path)
    image_source = source.content
    os.makedirs('images',exist_ok=True)

    with open(f'images/{name}-{i}.jpg', 'wb') as f:
        f.write(img_source)
    i +=1




