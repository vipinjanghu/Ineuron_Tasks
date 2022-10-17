# Task 2- @ vipin kumar
# Do a bulk load for these two table for respective dataset
import pandas as pd
import mysql.connector as conn

mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()


df1=pd.read_excel("Attribute DataSet.xlsx")
df2=pd.read_excel("Dress Sales.xlsx")
for i ,row in df1.iterrows():
    cursor.execute("insert into sql_practice_database.attribute_dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",tuple(row))
    mydb.commit()
for i,row in df2.iterrows():
    cursor.execute("insert into sql_practice_database.dress_dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",tuple(row))
    mydb.commit()

cursor.execute(("select count(*) from sql_practice_database.attribute_dataset"))
for i in cursor:
    print("Number of records in Attribute dataset: {}".format(i))

cursor.execute(("select count(*) from sql_practice_database.dress_dataset"))
for i in cursor:
    print("Number of records in Dress dataset: {}".format(i))