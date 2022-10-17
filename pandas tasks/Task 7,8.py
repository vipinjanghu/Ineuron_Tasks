import mysql.connector as conn
mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()
cursor.execute("use sql_practice_database")
cursor.execute("select count(distinct Dress_ID) from attribute_dataset")
for i in cursor:
    print("Number of unique dress:{}".format(i))

cursor2=mydb.cursor()
cursor2.execute("use sql_practice_database")
cursor2.execute("select count(Dress_ID) from attribute_dataset where Recommendation=0")
for i in cursor2:
    print("No of dresses having recommendation 0:{}".format(i))