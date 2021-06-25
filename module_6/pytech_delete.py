#Angela Perkins
#Module 6_3

#Accessing MongoDB pytech database
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.9olja.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

#Accessing the collection students
students = db.students

#search for all students in the database 
student_list = students.find({})
print("\n  -- All student documents returned with find() query --")
for doc in student_list:
#display information 
   print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#give it the student data
melmac = {
 "student_id": "1010",
 "first_name": "Melmac",
 "last_name": "Hodge"
}
#insert the student data 
melmac_1010 = students.insert_one(melmac).inserted_id

#locate the new student
melmac = students.find_one({"student_id": "1010"})

#display information
print("\n  -- Single student document returned with find_one() query --")
print(" Student ID: " + melmac["student_id"] + "\n First Name: " + melmac["first_name"] + "\n Last Name: " + melmac["last_name"] + "\n")


#remove the student
melmac = students.delete_one({"student_id": "1010"})

#search for all students in the database 
student_list = students.find({})
print("\n  -- All student documents returned with find() query --")
for doc in student_list:
#display information 
   print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")


