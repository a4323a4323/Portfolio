from flask import Flask
from flask import request
from werkzeug.user_agent import UserAgent #載入request物件
import json
# 建立 Application 物件，可設定靜態檔案的路徑處理
app=Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址路徑
    ) # 所有在static資料底下的檔案，都對應到網址路徑 / 檔案名稱

#--------------------------------------------------------

#建立路徑 /getsum 對應的處理函式
#利用要求字串 (query string)提供彈性 :/getsum?max=最大數字
@app.route("/getsum")
def getsum(): #1+2+....+max
    #接收要求字串中的參數資料
    maxnumber=request.args.get("max",100) #100是預設值
    maxnumber=int(maxnumber)
    minnumber=request.args.get("min",1) #1是預設值
    minnumber=int(minnumber)

    #以下運算 min+(min+1)+(min+2)+....+max 總和的迴圈邏輯
    result=0
    for n in range(minnumber,maxnumber+1):
        result+=n
    #把結果回應給前端
    return "結果:"+str(result)

#--------------------------------------------------------

#建立路徑 / 對應的回應方式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return json.dumps({
            "status":"ok",
            "text":"Hello world"
        })
    else:
        return json.dumps({
            "status":"ok",
            "text":"哈囉~你好呀!"
        },ensure_ascii=False) #指示不要用ascii編碼處理中文

#建立路徑 / data 對應的回應方式
@app.route("/data")
def handleData():
    return "My Data"
#--------------------------------------------------------

@app.route("/user/<username>")
def handleusername(username):
    if username=="于涵":
        return "你好呀" +username
    else:
        return "Hello" +username

#啟動網站伺服器，可透過port參數指定阜號
app.run(port=2000)
