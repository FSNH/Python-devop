import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.picture
collection = db.pic
collection.remove()
items = collection.find()
for item in items:
    print(item)
