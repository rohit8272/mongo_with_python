import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['student']
collection = db['marks']

#delete One 
# del_col = collection.delete_one({"name" : "virat"})
# print(del_col.deleted_count)


#delete_many
del_col = collection.delete_many({"name" : "rohit sharma"})
print(del_col.deleted_count)
