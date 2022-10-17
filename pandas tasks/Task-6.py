# task-6 @ vipin kumar

import mysql.connector as conn
mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()
cursor.execute("use sql_practice_database")
cursor.execute("select * from attribute_dataset as a left join dress_dataset as b on a.Dress_ID=b.Dress_ID")
for i in cursor:
    print(i)