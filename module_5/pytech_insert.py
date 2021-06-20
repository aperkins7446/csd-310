MongoDB: insert_one() 
fred = {
 "first_name": "Fred",
 "last_name": "Smith"
}
 
fred_1007 = students.insert_one(fred).inserted_id
 
print(fred_1007)

MongoDB: insert_one() 
hazel = {
 "first_name": "Hazel",
 "last_name": "Hodge"
}
 
hazel_1008 = students.insert_one(hazel).inserted_id
 
print(hazel_1008)
MongoDB: insert_one() 
angela = {
 "first_name": "Angela",
 "last_name": "Perkins"
}
 
angela_1009 = students.insert_one(angela).inserted_id
 
print(angela_1009)