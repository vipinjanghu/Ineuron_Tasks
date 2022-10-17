import mysql.connector as conn
mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()
cursor.execute("use sql_practice_database")
cursor.execute("select Dress_ID from(select Dress_ID,total,dense_rank() over(order by total desc) as `rank` from (select Dress_ID,`29/8/2013`+`31/8/2013`+`09/02/2013`+`09,04,2013`+`09/06/2013`+"
               "`09/08/2013`+`09/10/2013`+`09/12/2013`+`09/14/2013`+`09/16/2013`+`09/18/2013`+"
               "`09/20/2013`+`09/22/2013`+`09/24/2013`+`09/26/2013`+`09/28/2013`+`09/30/2013`+"
               "`10/02/2013`+`10/04/2013`+`10/06/2013`+`10/08/2013`+`10/10/2013`+`10/12/2013` as total "
               "from dress_dataset group by Dress_ID order by total desc ) as a) as c where c.`rank`=3")
for i in cursor:
    print(i)