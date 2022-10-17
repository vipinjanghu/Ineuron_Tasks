# Task 1-@ Vipin kumar
# Create a  table attribute dataset and dress dataset


import mysql.connector as conn
mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()
cursor.execute("create database if not exists sql_practice_database ")
cursor.execute("use sql_practice_database")
a="create table if not exists attribute_dataset(Dress_ID int(10) NOT NULL,Style   varchar(50),Price   varchar(50)," \
  "Rating float,Size   varchar(50),Season   varchar(50),NeckLine   varchar(50),SleevLength   varchar(50),Waiseline   varchar(50)," \
  "Material   varchar(50),FabricTypr   varchar(50),Decoration   varchar(50),Pattern_Type   varchar(50),Recommendation int(2))"

b="create table if not exists dress_dataset(`Dress_ID` int(10) NOT NULL,`29/8/2013` int,`31/8/2013` int,`09/02/2013` int,`09,04,2013` int,`09/06/2013` int,`09/08/2013` int,`09/10/2013` int,`09/12/2013` varchar(50),`09/14/2013` varchar(50)," \
  "`09/16/2013` varchar(50),`09/18/2013` varchar(50),`09/20/2013` varchar(50),`09/22/2013` varchar(50),`09/24/2013` int,`09/26/2013` float,`09/28/2013` int,`09/30/2013` float," \
  "`10/02/2013` float,`10/04/2013` float,`10/06/2013` int,`10/08/2013` float,`10/10/2013` float,`10/12/2013` int)"
cursor.execute(a)
cursor.execute(b)
cursor.execute("USE sql_practice_database")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)