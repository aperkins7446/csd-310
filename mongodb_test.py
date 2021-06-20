from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.9olja.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List--")
print(db.list_collection_names())