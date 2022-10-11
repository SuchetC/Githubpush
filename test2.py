import pymongo

client = pymongo.MongoClient("mongodb+srv://suchet:suchet@cluster0.dchsyn0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
         "name": "suchet",
         "email": "s@gmail.com",
          "sub": "DS"

}
database = client['myinfo']
collection = database["suchet"]
collection.insert_one(data)