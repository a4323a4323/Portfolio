from flask import Flask
from flask import request
from flask import redirect
import json

from app import index
# 建立 Application 物件，可設定靜態檔案的路徑處理
app=Flask(
    __name__,static_folder="static", static_url_path="/" ) 

#--------------------------------------------------------

#redirect例子
# @app.route("/")
# def index(): 
#     return redirect("https://www.google.com/") #導向谷哥網站

#--------------------------------------------------------

#建立路徑 /en/ 對應的回應方式
@app.route("/en/")
def index_english(): 
    return json.dumps({
            "status":"ok",
            "text":"Hello world"
        })
#建立路徑 /zh/ 對應的回應方式
@app.route("/zh/")
def index_chinese(): 
        return json.dumps({
            "status":"ok",
            "text":"哈囉~你好呀!"
        },ensure_ascii=False) #指示不要用ascii編碼處理中文


@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")

