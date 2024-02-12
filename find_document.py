import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['student']
collection = db['marks']

#find_one_element
# find_document = collection.find_one({"name" : "gill"})
# print(find_document)

#find_all_document
find_all_docs = collection.find({"age" : 26})
for stu in find_all_docs:
    print(stu)

