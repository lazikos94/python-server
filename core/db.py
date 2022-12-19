# database related stuff like connection
from pymongo import MongoClient
from config import settings
import asyncio
import motor.motor_asyncio
client = None
database =None
collection =None
client = MongoClient('mongodb://empedus.services:49694/')
database = client['test-database']
collection = database['test-collection']
collectionq = database['test-questionnaire']
# def mongoConnect():
#     try:
       
#         client = MongoClient('mongodb://empedus.services:49694/')
#         database = client['test-database']
#         collection = database['test-collection']
#         try:
#             print(client,database,collection)
#         except Exception:
#             print("Unable to connect to the server.")
#     except:
#         print('Failed')

# def getCollection():
#     post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"]}
    # posts = database['test-database']
    # post_id = posts.insert_one(post).inserted_id
    # print(post_id)
    
