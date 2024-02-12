import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['student']
collection = db['marks']

#update_one_value
# collection.update_one({"name":"rohit sharma"} , {"$set" : {"age" : 34}})


#update_all value
# prew_value = {"name" : "virat"} 
# new_value =  {"$set" : {"marks": 208 } }
# collection.update_many( prew_value , new_value )
