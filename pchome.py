import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


path="C:/Users/acer/Desktop/新增資料夾/chromedriver.exe"
driver=webdriver.Chrome(path)
# 發出網路請求
driver.get('https://ecshweb.pchome.com.tw/search/v3.3/')

#搜尋
search=driver.find_elements_by_css_selector("#keyword")[0]
search.send_keys("相機")
button=driver.find_elements_by_css_selector("#btn_search")[0]
button.click()
time.sleep(5)

# 取出網頁整頁內容
page_content = driver.page_source
sp=BeautifulSoup(page_content,"lxml")
# 印出網頁標題
print(driver.title)

product=[]
#印出商品
all=sp.select("#ItemContainer .col3f")
for alls in all:
    name=alls.select(".prod_name a")[0].text
    price=alls.select(".price_box .price span")[0].text

    data={}
    data["name"]=name
    data["price"]=price
    product.append(data)

#CSV標題
head=["name","price"]

#存檔
with open("pchome.csv","w",newline="",encoding="utf-8")as f:
    dict_writer = csv.DictWriter(f,head)
    #寫標題
    dict_writer.writeheader()
    #寫內文
    dict_writer.writerows(product)

with open("pchome.csv","r",newline="",encoding="utf-8")as f:
    rows=csv.reader(f)
    for row in rows:
        print(row)

# 關閉瀏覽器
driver.quit()
