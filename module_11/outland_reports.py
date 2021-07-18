#Group name: Charlie Group
#Members: Jacob Breault, Angela Perkins, Skyler Millburn, William Silknitter III, Cameron Frison
#7/18/2021
#Module 11.4 QUERIES FOR REPORTING Outland Adventures Script

#import statements
import mysql.connector
from datetime import datetime
from mysql.connector import errorcode

#database config object"""
config = {
    "user": "outland_adventures_user",
    "password": "Angel@84",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

#try/catch block for handling potential MySQL database errors 
try:
    
    
    db = mysql.connector.connect(**config) # connect to outland_adventures database.
    cursor = db.cursor()
    
    #Query for question 1 on inventory
    cursor.execute("SELECT inventory.gear_name, orders.gear_id, SUM(orders.quantity) AS Items_Ordered FROM orders JOIN inventory ON orders.gear_id = inventory.gear_id GROUP BY gear_id")
    #Get inventory results and display results
    inventory = cursor.fetchall()
    print("\n --Inventory Name and Quantity Ordered--")
    for item in inventory:
        print(" Gear Name: {} \n Order ID: {} \n Total of Gear Ordered: {}".format(item[0], item[1], item[2]))
        print("\n")
    
    #Query for question 2 on customers per trip
    cursor.execute("SELECT trek_history.trip_date, trek.trek_id, trek.trek_name, trek.country, COUNT(trek_history.customer_id) AS Customers_On_Trip FROM trek_history INNER JOIN trek ON trek.trek_id = trek_history.trek_id GROUP BY trek_id, trip_date")
    per_trip_customers = cursor.fetchall()
    print("\n --Customers on Each Trek--")
    for per_trip_customer in per_trip_customers:
        print(" Trek Date: {} \n Trek Name: {} \n Trek Country: {}\n Number of Customers on Trek: {}".format(per_trip_customer[0], per_trip_customer[2], per_trip_customer[3],  per_trip_customer[4]))
        print("\n")

    #Query 3 part 1- looking for items more than give years old
    cursor.execute("SELECT gear_id, gear_name, purchase_date FROM inventory WHERE YEAR (purchase_date) < 2016")
    old_gears = cursor.fetchall()
    print("\n --All Gear Purchased Before 2016--")
    for old_gear in old_gears:
        print(" Gear ID: {} \n Gear Name: {}\n Purchase Date: {} \n ".format(old_gear[0], old_gear[1], old_gear[2]))
        print("\n")  

    #Query 3 part 2- purchase date of all gear
    cursor.execute("SELECT gear_id, gear_name, purchase_date FROM inventory") 
    all_gears = cursor.fetchall()
    print("\n --All Gear Purchase Dates--")
    for all_gear in all_gears:
        print(" Gear ID: {} \n Gear Name: {}\n Purchase Date: {} \n ".format(all_gear[0], all_gear[1], all_gear[2]))
        print("\n")  

    #Group query idea- frequent trekkers! How many treks and how much spent per customer id
    cursor.execute("SELECT trek_history.customer_id, customers.f_name, customers.l_name, COUNT(trek_history.trek_history_id) AS Total_Treks, SUM(trek_history.trip_cost) AS total_trek_cost FROM trek_history JOIN customers ON customers.customer_id = trek_history.customer_id GROUP BY customer_id")
    frequent_trekkers = cursor.fetchall()
    print("\n --How Many Treks and How Much Spent Per Customer--")
    for frequent_trekker in frequent_trekkers:
        print(" Customer ID: {} \n Customer First Name: {}\n Customer Last Name: {} \n Total Treks: {} \n Total Spent: {} \n".format(frequent_trekker[0], frequent_trekker[1], frequent_trekker[2], frequent_trekker[3],frequent_trekker[4],))
        print("\n") 

    input("\n\n  Press any key to continue.")
    db.commit()
    
except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
    