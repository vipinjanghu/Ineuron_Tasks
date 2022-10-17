import mysql.connector as conn
import pandas as pd

mydb=conn.connect(host="localhost",user ="root",passwd="9971372013")
cursor=mydb.cursor()
cursor.execute("create database if not exists bank;create table if not exists panakj ("
               "RESTAURANT_SERIAL_NUMBER varchar(30),CLASSIFIER_PROBABILITY float,CLASSIFIER_PREDICTION int)")