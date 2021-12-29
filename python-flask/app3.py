from flask import Flask
from flask import request
from flask import render_template

# 建立 Application 物件，可設定靜態檔案的路徑處理
app=Flask(__name__,static_folder="public", static_url_path="/" ) 

#建立路徑/對應的處理函式
# @app.route("/")
# def index():
#     return render_template("index") #()是templates裡的文字檔 括弧裡選擇你要的檔案名稱

#建立路徑/對應的處理函式
@app.route("/")
def index():
    return render_template("index.html") #()是templates裡的文字檔 括弧裡選擇你要的檔案名稱

#建立路徑/對應的處理函式
@app.route("/page")
def page():
    return render_template("page.html") #()是templates裡的文字檔 括弧裡選擇你要的檔案名稱

#建立路徑/對應的處理函式
@app.route("/show")
def show():
    name=request.args.get("name","")
    return "歡迎光臨,"+name

@app.route("/calculate",methods=["POST"])
def calculate():
    #接收GET方法的query string
    #maxnumber=request.args.get("max",10)
    #接收POST方法的query string
    maxnumber=request.form["max"]
    maxnumber=int(maxnumber)
    result=0
    for i in range(1,maxnumber+1):
        result+=i
    return render_template("result.html",data=result)

#啟動網站伺服器，可透過port參數指定阜號
app.run(port=2000)   