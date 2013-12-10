
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
scores = db.grades


def find():

    print "find, reporting for duty"

    query = {'type':'homework'}

    try:

        cursor = scores.find(query)
        #cursor = scores.find(query).skip(4)
        #cursor = cursor.limit(1)

        #cursor = cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])



    except:
        print "Unexpected error:", sys.exc_info()[0]
    student_old = 0    
    for doc in cursor:
        student = doc['student_id']
        if student != student_old:
            print "remove Old doc \n"
            remove_review_date(old_doc['_id'])
            print old_doc    
        old_doc = doc
        student_old = student
        #print doc
def remove_review_date(id):
    print "\n\nremoving all review dates"

    # get a handle to the school database
    #db=connection.school
    #scores = db.scores
    try:
        scores.remove({'_id':id})

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise        


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
    
    try:
        doc = scores.find_one(query)
        
    except:
        print "Unexpected error:", sys.exc_info()[0]

    
    print doc


find()

