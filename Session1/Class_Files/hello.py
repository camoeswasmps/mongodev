#! /usr/bin/python
import bottle
import pymongo

@bottle.route('/')
def index():
    
    #Connect to MongoDB
    connection = pymongo.MongoClient('localhost',27017)
    
    #attach to the database
    db = connection.test 
    
    #handle to names colection
    names = db.names
    
    item = names.find_one()
    
    return '<b>Hello %s!</b>' % item['name']
bottle.run(host='localhost', port=8080)