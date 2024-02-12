import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['student']
collection = db['marks']

#insert one
# dictionary1 = {"name" : "nik jones" , "age": 22 , "marks" : 98}
# collection.insert_one(dictionary1)


#insert many
# list_of_dictionary_of_student = [
#     {"name": "virat" , "age" : 36 ,"marks" : 3 },
#     {"name" : "rohit"  , "age" : 37 ,"marks" : 264 },
#     {"name" : "gill"  , "age" : 26 ,"marks" : 99 },
#     {"name" : "iyer"  , "age" : 29 ,"marks" : 57 },
#     {"name" : "manish" , "age" : 30 ,"marks" : 40 },
# ]

# collection.insert_many(list_of_dictionary_of_student)