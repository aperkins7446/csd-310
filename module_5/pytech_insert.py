
#Angela Perkins
#Module 5_3

#import pymongo and MongoClient
import pymongo
from pymongo import MongoClient

#connect to the MongoDB
url= "mongodb+srv://admin:admin@cluster0.9olja.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
#tell it which database we are adding students to
db = client.pytech
students = db['students']

#give it the student data
fred = {
 "student_id": "1007",
 "first_name": "Fred",
 "last_name": "Smith"
}
#insert the student data 
fred_1007 = students.insert_one(fred).inserted_id
 
print(fred_1007)


hazel = {
 "student_id": "1008",
 "first_name": "Hazel",
 "last_name": "Hodge"
}
 
hazel_1008 = students.insert_one(hazel).inserted_id
 
print(hazel_1008)

angela = {
"student_id": "1009",
 "first_name": "Angela",
 "last_name": "Perkins"
}
 
angela_1009 = students.insert_one(angela).inserted_id
 
print(angela_1009)