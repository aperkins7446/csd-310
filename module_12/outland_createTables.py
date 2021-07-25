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
cursor.execute("DROP TABLE IF EXISTS customer_rentals")
cursor.execute("DROP TABLE IF EXISTS customer_purchases")
cursor.execute("DROP TABLE IF EXISTS order_details")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS employee_trek_history")
cursor.execute("DROP TABLE IF EXISTS trek_history")
cursor.execute("DROP TABLE IF EXISTS trek")
cursor.execute("DROP TABLE IF EXISTS inventory")
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS customers")

"""Create tables"""
cursor.execute("CREATE TABLE customers (customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, f_name VARCHAR(75) NOT NULL, l_name VARCHAR(75) NOT NULL, address VARCHAR(75) NOT NULL, city VARCHAR(75) NOT NULL, state VARCHAR(75) NOT NULL, zip_code VARCHAR(75) NOT NULL, phone VARCHAR(75) NOT NULL)")
cursor.execute("CREATE TABLE trek (trek_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, trek_name VARCHAR(75) NOT NULL, country VARCHAR(75) NOT NULL, requires_visa BOOLEAN NOT NULL, required_immunizations BOOLEAN NOT NULL)")
cursor.execute("CREATE TABLE trek_history (trek_history_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, customer_id INT NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(customer_id), trek_id INT NOT NULL, FOREIGN KEY (trek_id) REFERENCES trek(trek_id), trip_cost DOUBLE NOT NULL, trip_date DATETIME NOT NULL)")
cursor.execute("CREATE TABLE inventory (gear_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, gear_name VARCHAR(75) NOT NULL, for_rent BOOLEAN NOT NULL, purchase_date DATETIME NOT NULL)") 
cursor.execute("CREATE TABLE orders (order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, trek_history_id INT NOT NULL, FOREIGN KEY(trek_history_id) REFERENCES trek_history(trek_history_id), order_date DATETIME NOT NULL)") 
cursor.execute("CREATE TABLE order_details ( order_details INT NOT NULL AUTO_INCREMENT PRIMARY KEY, order_id INT NOT NULL, FOREIGN KEY(order_id) REFERENCES orders(order_id), gear_id INT NOT NULL, FOREIGN KEY(gear_id) REFERENCES inventory(gear_id), purchase_cost DOUBLE NOT NULL, rental_cost DOUBLE NOT NULL)") 
cursor.execute("CREATE TABLE employees (employee_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, f_name VARCHAR(75) NOT NULL, l_name VARCHAR(75) NOT NULL, date_of_birth DATETIME NOT NULL, title VARCHAR(75) NOT NULL, supervisor_id INT NOT NULL)") 
cursor.execute("CREATE TABLE employee_trek_history (trek_history_id INT NOT NULL, FOREIGN KEY(trek_history_id) REFERENCES trek_history(trek_history_id), employee_id INT NOT NULL, FOREIGN KEY(employee_id) REFERENCES employees(employee_id), supervisor_id INT NOT NULL, FOREIGN KEY(supervisor_id) REFERENCES employees(employee_id))") 
cursor.execute("SHOW TABLES")

print("----Displaying Tables----")
for x in cursor:
    print(x)

cursor.execute("DROP VIEW IF EXISTS customer_spending")
cursor.execute("DROP VIEW IF EXISTS trek_rental_purchases")

"""Create views"""
cursor.execute("CREATE VIEW customer_spending AS SELECT customers.customer_id, customers.f_name, customers.l_name, th.number_of_treks, th.total_trip_cost, COUNT(CASE WHEN order_details.purchase_cost > 0 THEN 1 END) AS total_purchases, IFNULL(SUM(order_details.purchase_cost), 0) AS total_purchase_cost, COUNT(CASE WHEN order_details.rental_cost > 0 THEN 1 END) AS total_rentals, IFNULL(SUM(order_details.rental_cost), 0) AS total_rental_cost, (IFNULL(SUM(order_details.purchase_cost), 0) + IFNULL(SUM(order_details.rental_cost), 0) + th.total_trip_cost) as total_cost FROM ( SELECT trip_date, trek_id, customer_id, trek_history_id, COUNT(trip_date) as number_of_treks, SUM(trip_cost) as total_trip_cost FROM trek_history GROUP BY customer_id) AS th INNER JOIN customers ON customers.customer_id = th.customer_id LEFT JOIN orders ON th.trek_history_id = orders.trek_history_id LEFT JOIN order_details ON orders.order_id = order_details.order_id GROUP BY customers.customer_id ORDER BY total_cost DESC;")
cursor.execute("CREATE VIEW trek_rental_purchases AS SELECT trek_history.trip_date, trek_history.trek_id, trek.trek_name, COUNT(CASE WHEN order_details.purchase_cost > 0 THEN 1 END) AS total_purchases, IFNULL(SUM(order_details.purchase_cost), 0) AS total_purchase_cost, COUNT(CASE WHEN order_details.rental_cost > 0 THEN 1 END) AS total_rentals, IFNULL(SUM(order_details.rental_cost), 0) AS total_rental_cost, (IFNULL(SUM(order_details.purchase_cost), 0) + IFNULL(SUM(order_details.rental_cost), 0)) as total_cost FROM trek_history LEFT JOIN orders ON trek_history.trek_history_id = orders.trek_history_id LEFT JOIn order_details ON orders.order_id = order_details.order_id INNER JOIN trek ON trek_history.trek_id = trek.trek_id GROUP BY trip_date, trek_id ORDER BY trek_history.trip_date ASC;")

cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS")
print("----Displaying Views----")
for x in cursor:
    print(x)