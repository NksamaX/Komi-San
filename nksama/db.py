import pymongo
import os

MONGO_URL = os.environ.get('MONGO_URL')

database = pymongo.MongoClient(MONGO_URL)['notes']['notes']
