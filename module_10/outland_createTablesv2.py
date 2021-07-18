#Group name: Charlie Group
#Members: Jacob Breault, Angela Perkins, Skyler Millburn, William Silknitter III, Cameron Frison
#7/10/2021
#Module 10.2 CREATE TABLES Outland Adventures Script

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
mydb = mysql.connector.connect(
    host = "localhost",
    user = "outland_adventures_user",
    password = "Angel@84",
    database = "outland_adventures"
)

"""Create cursor"""
cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS trek")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS employee_trek_history")
cursor.execute("DROP TABLE IF EXISTS trek_history")
cursor.execute("DROP TABLE IF EXISTS inventory")
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS customers")

"""Create tables"""
cursor.execute("CREATE TABLE customers (customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, f_name VARCHAR(75) NOT NULL, l_name VARCHAR(75) NOT NULL, address VARCHAR(75) NOT NULL, city VARCHAR(75) NOT NULL, state VARCHAR(75) NOT NULL, zip_code VARCHAR(75) NOT NULL, phone VARCHAR(75) NOT NULL)")
cursor.execute("CREATE TABLE trek_history (trek_history_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, customer_id INT NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(customer_id), trek_name VARCHAR(75) NOT NULL, trip_cost DOUBLE NOT NULL, trip_date DATETIME NOT NULL)")
cursor.execute("CREATE TABLE trek (trek_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, trek_name VARCHAR(75) NOT NULL, country VARCHAR(75) NOT NULL, requires_visa BOOLEAN NOT NULL, required_immunizations BOOLEAN NOT NULL)")
cursor.execute("CREATE TABLE inventory (gear_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, gear_name VARCHAR(75) NOT NULL, for_rent BOOLEAN NOT NULL, purchase_date DATETIME NOT NULL)") 
cursor.execute("CREATE TABLE orders (order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, trek_history_id INT NOT NULL, FOREIGN KEY(trek_history_id) REFERENCES trek_history(trek_history_id), customer_id INT NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(customer_id), gear_id INT NOT NULL, FOREIGN KEY(gear_id) REFERENCES inventory(gear_id), quantity INT NOT NULL, order_cost DOUBLE NOT NULL, order_date DATETIME NOT NULL)") 
cursor.execute("CREATE TABLE employees (employee_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, f_name VARCHAR(75) NOT NULL, l_name VARCHAR(75) NOT NULL, date_of_birth DATETIME NOT NULL, title VARCHAR(75) NOT NULL, supervisor_id INT NOT NULL UNIQUE)") 
cursor.execute("CREATE TABLE employee_trek_history (trek_history_id INT NOT NULL, FOREIGN KEY(trek_history_id) REFERENCES trek_history(trek_history_id), employee_id INT NOT NULL, FOREIGN KEY(employee_id) REFERENCES employees(employee_id), supervisor_id INT NOT NULL, FOREIGN KEY(supervisor_id) REFERENCES employees(supervisor_id))") 
cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)