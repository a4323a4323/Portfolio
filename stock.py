from bs4 import BeautifulSoup
import requests as req
import pandas as pd
data=[]
number=int(input("請輸入股票代號"))
url="https://tw.stock.yahoo.com/quote/{}.TW".format(number)
r=req.get(url)
sp=BeautifulSoup(r.text,"lxml")

name=sp.find("h1",class_="Fw(b)")
data.append([name.text])

num=sp.find_all("li",class_="price-detail-item")
for nums in num:
    data.append([nums.text])

time=sp.find("span",class_="Fz(14px)")
data.append([time.text])

print(data)

df=pd.DataFrame(data)
df.to_csv("stock.csv",index=False,encoding="utf-8")
