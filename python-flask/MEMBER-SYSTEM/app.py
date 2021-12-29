import pymongo
from flask import *

#初始化資料庫連線
client=pymongo.MongoClient("mongodb+srv://root:root123456@cluster0.izadf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.member_system

#初始化 Flask 伺服器
app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret"


#路由處理
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "nickname" in session:   
        return render_template("member.html")
    else:
        return redirect("/")
#/error?msg=
@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤，請聯繫客服")
    return render_template("error.html",message=message)

@app.route("/signup",methods=["POST"])
def signup():
    #從前端接收資料
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    #根據收到的資料，和資料互動
    collection=db.user
    #檢查會員集合中，是否有相同的信箱文件資料
    result=collection.find_one({
        "email":email
    })
    if result!=None:
        return redirect("/error?msg=信箱已被註冊")
    #把資料放進資料庫，完成註冊
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "passsword":password
    })
    return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    #從前端接收資料
    email=request.form["email"]
    password=request.form["password"]
    #和資料庫互動
    collection=db.user
    #檢查帳密是否相同
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    #找不到對應資料，登入失敗，導向錯誤頁面
    if result==None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    #登入成功，在Session紀錄會員資訊，導向會員頁面
    session["nickname"]=result["nickname"]
    return redirect("/member")

@app.route("/signout")
def signout():
    #移除session中的會員資訊
    del session["nickname"]
    return redirect("/")

app.run(port=2000)