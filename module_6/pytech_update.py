#Angela Perkins
#Module 6_2

#Accessing MongoDB pytech database
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.9olja.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

#Accessing the collection students
students = db.students

#search for all students in the database (basically our queries assignment)
student_list = students.find({})
print("\n  -- All student documents returned with find() query --")
for doc in student_list:
#display information 
   print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#update a student
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Hodge"}})

#locate the updated student
fred = students.find_one({"student_id": "1007"})

#display information 
print("\n  -- Single student document returned with find_one() query --")
print("  Student ID: " + fred["student_id"] + "\n  First Name: " + fred["first_name"] + "\n  Last Name: " + fred["last_name"] + "\n")
