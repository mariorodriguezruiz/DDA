'''
Created on 29 may. 2017

@author: Mario
'''
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Bonus7']
collection = db['students']

# ----------- TASK 1 --------------
cur = collection.find({}, {"name.last":1, "course_gpas":{"$slice": [5, 5]}})
  
# for doc in cur:
#     print(doc)  
    
    
# ----------- TASK 2 --------------
cur = collection.find({"test_scores": {'$elemMatch':{"test": "SAT", "score":{"$gt":700} }}}, 
                      {"name.last":1, "test_scores": {"$slice": -1}}).sort("test_scores.score",-1)
                      
                      
# ----------- TASK 3 --------------          

# Add new empty list called evaluations:[]
cur = collection.updateMany({}, { "$set" : {"evaluation":[]} })
# Add "eval comment": "This student is very clever" in "evaluation"
cur = collection.updateMany({},{ "$push" : {"evaluation.0.eval_comment":"This student is very clever"}} 
)
# Add "eval comment": "This student always submits exercises ontime" in "evaluation"
cur = collection.updateMany({}, {"$push": {"evaluation.0.eval_comment":"This student always submits exercises ontime"}} 
)

da = collection.find({}, {"evaluation.eval_comment":1})
                     
for doc in da:
    print(doc) 