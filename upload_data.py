
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://aniket32126440:<password>@aniket0.pd4hhgg.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
#

#create database name and collection
DATABASE_NAME='pwskills'
COLLECTION_NAME='waferfault'

#read the data as a dataframe
df=pd.read_csv('E:\MLProjectsPW\sensorfault\notebooks\wafer_23012020_041211.csv')
df=df.drop('Unnamed: 0',axis=1)


#turn the dataframe into json
json_record=json.load(df.T.to_json)

json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

# Send a ping to confirm a successful connection


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)