from flask import Flask
from flask import request
from flask import session
from flask import render_template

# 建立 Application 物件，可設定靜態檔案的路徑處理
app=Flask(__name__,static_folder="public",static_url_path="/")

app.secret_key="any string but secret" #設定session的密鑰

@app.route("/")
def index():
    return render_template("index2.html")

#使用GET方法處理路徑 /hello?name=使用者名字
@app.route("/hello")
def hello():
    name=request.args.get("name","")
    session["username"]=name #session ["欄位名稱"]=資料
    return "哈囉~"+name

#使用GET方法處理路徑 /talk
@app.route("/talk")
def talk():
    name=session["username"]
    return "有甚麼事呀?"+name

app.run(port=2000)