from flask import Flask,request,jsonify
import pymongo


app=Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://vipinjanghu:987456321@cluster0.njqxn2h.mongodb.net/?retryWrites=true&w=majority")
db = client["Pandas"]
collection=db["test1"]
@app.route("/insert",methods=['POST'])
def insert():
    if (request.method=='POST'):
        a=request.json['name']
        b=request.json['age']
        c=request.json['number']
        d={'Name':a,'Age':b,'Number':c}
        collection.insert_one(d)
        return jsonify(str("Successfuly inserted"))

@app.route("/update",methods=['POST'])
def update():
    if (request.method=='POST'):
        a=request.json['name']
        b=request.json['age']
        collection.update_one({"Name":a},{"$set":{"Age":b}})
    return jsonify(str("Successfuly updated"))


@app.route("/delete",methods=['POST'])
def delete():
    if(request.method=='POST'):
        a = request.json['name']
        b = request.json['age']
        collection.delete_one({"Name":a,"Age":b})
        return jsonify(str("Successfuly deleted"))

@app.route("/find",methods=['POST'])
def find():
    if(request.method=='POST'):
        a=request.json['name']
        b=request.json['age']
        c=request.json['number']
        x=collection.find_one({'Name':a,'Age':b,'Number':c})
        return jsonify(str(x))
if __name__=='__main__':
    app.run()