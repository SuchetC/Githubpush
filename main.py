import pymongo

client = pymongo.MongoClient("mongodb+srv://suchi:suchi123@cluster0.3sjw7zw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# d = {
#     "name": "suchet",
#     "email": "suchetc0@gmail.com",
#     "surname": "channagiri"
#
# }
# db1 = client['mongotest']
# coll = db1['test']
# coll.insert_one(d )


d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

