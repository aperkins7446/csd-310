MongoDB: find() 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() 
doc = db.collection_name.find_one({"student_id": 1007})
 
print(doc[1007])

MongoDB: find_one() 
doc = db.collection_name.find_one({"student_id": 1008})
 
print(doc[1008])

MongoDB: find_one() 
doc = db.collection_name.find_one({"student_id": 1009})
 
print(doc[1009])