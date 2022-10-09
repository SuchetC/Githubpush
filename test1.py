import pymongo

client = pymongo.MongoClient("mongodb+srv://suchet:suchet@cluster0.dchsyn0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "suchet",
    "email": "suchetc0@gmail.com",
    "surname": "channagiri"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )