import pymongo

client = pymongo.MongoClient("mongodb+srv://suchet:suchet@cluster0.dchsyn0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#print(db)

data = {
         "name": "suchet",
         "email": "s@gmail.com",
          "sub": "DS"

}

list_Of_record = [
    {
        "name":"suchet",
        "age":24
    },
    {
        "name":"sam",
        "age":14
    },
    {
        "name":"raj",
        "age":24
    }

]

database = client['myinfo']
collection = database["suchet"]
#collection.insert_one(data)

#collection.insert_many(list_Of_record)


# record = collection.find()
# for i in record:
#     print(i)

# data = collection.find({"name" : "sam"})
# for i in data:
#     print(i)

data = collection.find({"name" : {"$lt":"Z"}})