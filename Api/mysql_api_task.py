from flask import Flask,request,jsonify
import mysql.connector as conn


app=Flask(__name__)
db = conn.connect(host="localhost", user="root", password="9971372013")
curser = db.cursor()
curser.execute("create database if not exists api")
curser.execute("use api ")
curser.execute("create table if not exists testapi(name varchar(10),age float)")
@app.route("/sqlinsert",methods=['GET','POST'])
def sql_insert():
    if (request.method=='POST'):

        ab=request.json['name1']
        b=request.json['age1']
        sq="insert into testapi values (%s,%s)"
        val=(ab,b)
        curser.execute(sq,val)
        db.commit()

        return jsonify(ab,str(b))


@app.route("/update",methods=['GET','POST'])
def update():
    if(request.method=='POST'):

        a=request.json['name1']
        b=request.json['age1']
        sq=f"update testapi set age= '{b}' where name =  '{a}'"
        curser.execute(sq)
        db.commit()

        return jsonify(str(a),str(b))



@app.route("/delete",methods=['GET','POST'])
def delete():
    if(request.method=='POST'):

        a=request.json['name1']
        b = request.json['age1']
        sq=f"delete from testapi where name = '{a}' and age='{b}'"
        curser.execute(sq)
        db.commit()

        return jsonify(str(a),str(b))

@app.route("/featch",methods=['GET','POST'])
def featch():
    if(request.method=='POST'):

        a=request.json['name1']
        b=request.json['age1']
        sq=f"select * from testapi where name='{a}' and age='{b}'"
        curser.execute(sq)
        c = []
        for i in curser:

            c.append(i)
        return jsonify(c)
if __name__=='__main__':
    app.run()