from dotenv import load_dotenv 
load_dotenv()
import os 
password = os.environ.get("password") 

import pymongo
from pymongo.mongo_client import MongoClient
import os ,sys 
import pandas as pd 
from ensure import ensure_annotations 
from typing import Any 



class  mongodb_operation:
    def __init__(self ,client_url :str , database_name :str ,collection_name :str):
        self.client_url = client_url 
        self.database_name = database_name 
        self.collection_name = collection_name 
    
    def create_client(self):
        client = MongoClient(self.client_url) 
        return client
    
    def create_database(self):
        client = self.create_client()
        database = client[self.database_name]
        return database 
    
    def create_collection(self ,collection_name=None):
        database = self.create_database()
        collection = database[collection_name]
        return collection  
    
    def insert_record(self ,record ,collection_name :str):
        collection = self.create_collection(collection_name = collection_name)
        
        if type(record) == list:
            for data in record:
                 if type(data)!= dict:
                     raise TypeError('Record must be in dictionary')
            collection.insert_many(record) 
        elif type(record) == dict:
            collection.insert_one(record)

    def bulk_insert(self ,datafile_path :str ,collection_name :str):
        
        self.path = datafile_path 
        
        if self.path.endswith('csv',encoding='utf-8'):
            data = pd.read_csv(self.path)
            
        elif self.path.endswith('xlsx'):
            data = pd.read_excel(self.path ,encoding='utf-8')
            
        datajson = json.load(data.to_json(orient='records'))
        collection = self.create_collection()
        collection.insert_many(datajson) 
        
    def find_all(self,collection_name :str):
        collection = self.create_collection(collection_name=collection_name)
        data =collection.find()
        return data
