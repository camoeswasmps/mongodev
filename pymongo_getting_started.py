import pymongo

from pymongo import MongoClient

#Conection to the Database
connection = MongoClient('localhost',27017)

db = connection.test

#handle to names colection

names = db.names

item = names.find_one()

print item['name']
