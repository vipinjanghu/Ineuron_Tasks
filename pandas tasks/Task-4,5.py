import pandas as pd
df=pd.read_excel("Attribute DataSet.xlsx")

import pymongo
client = pymongo.MongoClient("mongodb+srv://vipinjanghu:987456321@cluster0.njqxn2h.mongodb.net/?retryWrites=true&w=majority")
db = client["json_initial"]
collection=db["test2"]

collection.insert_many(df.to_dict("records"))

# 2nd method
# df=pd.read_excel("Attribute Dataset.xlsx")
# json_format=df.to_json(orient='records')
# import json
# json_format=json.loads(json_format)
# collection.insert_many(json_format)