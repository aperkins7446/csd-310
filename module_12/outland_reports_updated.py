#Group name: Charlie Group
#Members: Jacob Breault, Angela Perkins, Skyler Millburn, William Silknitter III, Cameron Frison
#7/23/2021
#REVISED QUERIES FOR REPORTING Outland Adventures Script

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
    
    #Query for question 1 purchases versus rentals
    cursor.execute("SELECT * FROM trek_rental_purchases")
    #Get results items and costs of purchases and rentals per trip and display results
    trek_inventory = cursor.fetchall()
    print("\n --Inventory Name and Quantity Ordered--")
    for trek_item in trek_inventory:
        print(" Trip Date: {} \n Trek ID: {} \n Trek Name: {} \n Total Purchases {}  \n Total Purchases Cost: ${}  \n Total Rentals: {} \n Total Rental Cost: ${}  \n Amount Spent on Purchases and Rentals for Trek: ${}".format(trek_item[0], trek_item[1], trek_item[2], trek_item[3], trek_item[4], trek_item[5], trek_item[6], trek_item[7]))
        print("\n")
    #Query for question 1 in a summary form of purchase totals and costs vs rental totals and costs
    cursor.execute("SELECT SUM(total_purchases) as summary_purchases, SUM(total_purchase_cost) as summary_purchase_cost, SUM(total_rentals) as summary_rentals, SUM(total_rental_cost) as summary_rental_cost FROM trek_rental_purchases")
    #Get inventory results and display results
    summary_inventory = cursor.fetchall()
    print("\n --Summary of Total Number and Cost of Purchases vs Rentals--")
    for summary_item in summary_inventory:
        print(" Total Number of Purchases: {} \n Total Cost of Purchases: ${} \n Total Number of Rentals: {} \n Total Cost of Rentals: ${}".format(summary_item[0], summary_item[1], summary_item[2], summary_item[3]))
        print("\n")
    
    #Query for question 2 on customers per trip
    cursor.execute("SELECT trek_history.trip_date, trek.trek_id, trek.trek_name, trek.country, COUNT(trek_history.customer_id) AS Customers_On_Trip FROM trek_history INNER JOIN trek ON trek.trek_id = trek_history.trek_id GROUP BY trek_id, trip_date")
    per_trip_customers = cursor.fetchall()
    print("\n --Customers on Each Trek--")
    for per_trip_customer in per_trip_customers:
        print(" Trek Date: {} \n Trek Name: {} \n Trek Country: {}\n Number of Customers on Trek: {}".format(per_trip_customer[0], per_trip_customer[2], per_trip_customer[3],  per_trip_customer[4]))
        print("\n")

    #Query 3 find for items more than give years old
    cursor.execute("SELECT gear_id, gear_name, purchase_date FROM inventory WHERE YEAR (purchase_date) < 2016")
    old_gears = cursor.fetchall()
    print("\n --All Gear Purchased Before 2016--")
    for old_gear in old_gears:
        print(" Gear ID: {} \n Gear Name: {}\n Purchase Date: {} \n ".format(old_gear[0], old_gear[1], old_gear[2]))
        print("\n")  
    

    #Query 3 part 2- total number of piece vs total number of pieces older than 5
    cursor.execute("SELECT COUNT(gear_id) as gear_count FROM inventory WHERE YEAR (purchase_date) < 2016") 
    summary_old_gears = cursor.fetchall()
    print("\n --Inventory Over 5 Years vs Total Inventory vs --")
    for summary_old_gear in summary_old_gears:
        print("Total Items Over 5 Years Old: {} ".format(summary_old_gear[0]))
    cursor.execute("SELECT COUNT(gear_id) as gear_count FROM inventory") 
    summary_gears = cursor.fetchall()
    for summary_gear in summary_gears:
        print("Total Number of Items: {} \n ".format(summary_gear[0]))


    #Group query idea- Top spenders! The top three biggest spenders of our current customers
    cursor.execute("SELECT f_name, l_name, total_cost, number_of_treks, total_trip_cost, total_purchases, total_purchase_cost, total_rentals, total_rental_cost FROM customer_spending ORDER BY total_cost DESC LIMIT 3")
    top_trekkers = cursor.fetchall()
    print("\n --Customers: Our Top Three Total Spenders--")
    for top_trekker in top_trekkers:
        print(" Customer First Name: {}\n Customer Last Name: {} \n Total Spent with Outland Adventures: ${} \n Total Treks: {} \n Total Spent on Trips: ${} \n Total Purchases: {} \n Total Spent on Purchases: ${} \n Total Rentals: {} \n Total Spent on Rentals: ${} \n".format(top_trekker[0], top_trekker[1], top_trekker[2], top_trekker[3],top_trekker[4], top_trekker[5],top_trekker[6],top_trekker[7],top_trekker[8]))
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
    