
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.school
scores = db.students


def find_id():

    print "find_id, reporting for duty"

    query = {}
    selector = {'_id':1}


    try:

        cursor = scores.find(query,selector)
        for doc in cursor:
            print doc
            id = doc['_id']
            remove_review_homework(id)
    except:
        print "Unexpected error:", sys.exc_info()[0]

def remove_review_homework(id):
    print "Reviewing Homework"
    print id
    small_score = -1
    query = {'_id':id}  
    
    
    try:
        student = scores.find_one(query)

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise        
    
    print student
    score_list = student['scores']
    print "Score List: "
    print score_list
    for score in score_list:
        if score['type'] != 'homework':
            continue
        if small_score == -1:
            small_score = score['score']
            continue
        if small_score > score['score']:
            small_score = score['score']
    
    print "the small value is: "
    print small_score
    
    for smaler in score_list:
        if smaler['score'] == small_score:    
            score_list.remove(smaler)
    
    print score_list
    update_score(id,score_list)
    
    
def update_score(id,new_scores):

    try:
        # update using set
        scores.update({'_id':id},
                      {'$set':{'scores':new_scores}})

        score = scores.find_one({'_id':id})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise    
    

find_id()

