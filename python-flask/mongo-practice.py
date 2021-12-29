import pymongo
from bson.objectid import ObjectId


#連線到MongoDB 雲端資料庫
client=pymongo.MongoClient("mongodb+srv://root:root123456@cluster0.izadf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#把資料放進資料庫
db=client.website #選擇操作 website 資料庫
collection=db.member #選擇操作 member 集合

#把資料新增到集合中(一次新增多筆many)
# result=collection.insert_many([
#     {"name":"美美",
#     "email":"ccc@ccc.com",
#     "password":"ccc",
#     "level":1},

#     {"name":"小明",
#     "email":"fff@fff.com",
#     "password":"fff",
#     "level":3}
# ])
#取得新增資料的編號
# print(result.inserted_ids)

#取得集合中的第一筆資料
# data=collection.find_one()
# print(data)

#根據ObjectID 取得文件資料
# data=collection.find_one(
#     ObjectId("618e0274977f69a0f98d0899")
# )
# print(data)

#取得文件資料中的欄位
# print(data["email"])

#一次取得多筆文件資料
# cursor=collection.find()
# for doc in cursor:
#     print(doc)

#更新集合中的一筆資料
# result=collection.update_one({
#     "email":"fff@fff.com"},
#     {"$set":{"level":3}
# })

#更新集合中的多筆資料
# result=collection.update_many({
#     "level":5},
#     {"$set":{"level":8}
# })

# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)

#刪除集合中的一筆資料
# result=collection.delete_one({
#     "name":"美美"
# })

#刪除集合中的多筆資料
# result=collection.delete_many({
#     "level":2
# })
# print("實際上刪除的資料有幾筆:",result.deleted_count)

#篩選集合中的文件資料
# data=collection.find_one({
#     "email":"sss@sss.com"
# })
# print("取得的資料",data)

#複合篩選條件
# data=collection.find_one({
#     "$and":[
#         {"name":"小明"},
# {"email":"fff@fff.com"}
#     ]
# })
# print("取得的資料",data)
#篩選結果排序
data=collection.find({
    "$or":[
        {"email":"fff@fff.com"},
        {"level":1}
    ]},sort=[
        ("level",pymongo.DESCENDING)
    ])
for i in data:
    print("取得的資料",i)