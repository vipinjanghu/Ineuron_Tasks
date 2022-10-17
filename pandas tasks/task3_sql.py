# Task 3-@Vipin kumar
# read these dataset in pandas as a dataframe
import pandas as pd
import mysql.connector as conn

mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()

#getting column names from mysql table
cursor.execute("show columns from sql_practice_database.attribute_dataset ")
attribute_column=[]
for i in cursor:
    attribute_column.append(i[0])
# Getting sql table and store inside a dataframe
cursor.execute("select * from sql_practice_database.attribute_dataset ")
df1=pd.DataFrame(cursor.fetchall(),columns=attribute_column)
print(df1.head())


#getting column names for dress dataset from mysql table
cursor.execute("show columns from sql_practice_database.dress_dataset ")
dress_column=[]
for i in cursor:
    dress_column.append(i[0])
# Getting sqldress table and store inside a dataframe
cursor.execute("select * from sql_practice_database.dress_dataset ")
df2=pd.DataFrame(cursor.fetchall(),columns=dress_column)
print(df2.head())