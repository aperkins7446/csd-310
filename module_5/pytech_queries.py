
#Angela Perkins
#Module 5_3

#import pymongo and MongoClient
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.9olja.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
#tell it which database we want to look at
db = client.pytech
students = db.students

#search for all students in the database
student_list = students.find({})
print("\n  -- All student documents returned with find() query --")
for doc in student_list:
#display information 
   print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#search for one student in the database
hazel = students.find_one({"student_id": "1008"})
#display information
print("\n  -- Single student document returned with find_one() query --")
print("  Student ID: " + hazel["student_id"] + "\n  First Name: " + hazel["first_name"] + "\n  Last Name: " + hazel["last_name"] + "\n")


