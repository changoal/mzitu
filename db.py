import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['wallhaven']
collection = db['wall']

data = collection.find().limit(10)

for d in data:
    d['favourites'] = int(d['favourites'])
    d['Views'] = int(d['Views'])