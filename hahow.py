import requests as req
from openpyxl import Workbook

wb=Workbook() #創建excel檔案
ws=wb.active #預設工作表
title=['課名','老師','售價','預購價','販售數']
ws.append(title) #在試算表中加入標題

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
for index in range(28):
        url="https://api.hahow.in/api/courses?limit=24&page="
        url=url+str(index)
        print(url)
        r=req.get(url, headers=headers)
        print(r)

        root_json=r.json()
        for data in root_json['data']:
            course=[]
            course.append(data["title"])
            course.append(data["owner"]["name"])
            course.append(data["price"])
            course.append(data["preOrderedPrice"])
            course.append(data["numSoldTickets"])

            ws.append(course)

wb.save("data.xlsx")
