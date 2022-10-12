import pymongo

client = pymongo.MongoClient("mongodb+srv://suchet:suchet@cluster0.dchsyn0.mongodb.net/?retryWrites=true&w=majority")
db = client.test


# data = collection.find({"name" : "sam"})
# for i in data:
#     print(i)


data = [
    {"item":"laptop", "qty": 25, "status":"a"},
    {"item": "mobil", "qty": 85, "status": "b"},
    {"item": "mouse", "qty": 120, "status": "b"},
    {"item": "pen", "qty": 245, "status": "c"},
]

database = client['inventory']
collection = database['store']
#collection.insert_many(data)

#d= collection.find({'status': {'$in': ['a','b']} })

#d= collection.find({'status': {'$gte':'a'} })

#d= collection.find({'item':'pen' , 'status':'c'})

#d= collection.find({'item':'pen' , 'qty':{'$gt':100}})

# d= collection.find({'$or':  [{'item':'pen'},{'qty':245}]  })    #or

# collection.delete_one({'item':'pen'})
collection.update_one({'status':'b'}, {'$set':  {'status': 'new_b'} })
d= collection.find()
for i in d:
    print(i)


