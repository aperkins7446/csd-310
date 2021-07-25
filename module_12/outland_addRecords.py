#Group name: Charlie Group
#Members: Jacob Breault, Angela Perkins, Skyler Millburn, William Silknitter III, Cameron Frison
#7/11/2021
#Module 10.3 ADD RECORDS Outland Adventures Script

"""import statements"""
import mysql.connector
from datetime import datetime
from mysql.connector import errorcode

"""database config object"""
config = {
    "user": "outland_adventures_user",
    "password": "Angel@84",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

""" try/catch block for handling potential MySQL database errors """ 
try:
    
    
    db = mysql.connector.connect(**config) # connect to outland_adventures database.
    cursor = db.cursor()
    
    """Truncate all tables; makes sure we have empty tables before entering data"""
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE inventory")
    cursor.execute("TRUNCATE employee_trek_history")
    cursor.execute("TRUNCATE trek_history")
    cursor.execute("TRUNCATE trek")
    cursor.execute("TRUNCATE orders")
    cursor.execute("TRUNCATE order_details")
    cursor.execute("TRUNCATE employees")
    cursor.execute("TRUNCATE customers")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    """Executemany values into customers table"""
    customerSQL = "INSERT INTO customers(f_name, l_name, address, city, state, zip_code, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    customerRecord = [
        ('John', 'Smith', '123 Apple Street', 'Bigcity', 'Indiana', '12345', '123-456,7890'),
        ('Lily', 'Smith', '123 Apple Street', 'SmallCity', 'Kentucky', '54321', '098-765-4321'),
        ('Jake', 'Johnson', '456 Pear Ave', 'MedCity', 'Ohio', '44444', '111-111-1111'),
        ('Mary', 'Lee', '555 Orange Rd', 'OtherCity', 'Florida', '22222', '222-222-2222'),
        ('Thomas', 'Jones', '999 West St', 'Sidecity', 'Arizona', '66666', '999-999-9999'),
        ('Isacc', 'Lee', '555 Orange Rd', 'OtherCity', 'Florida', '22222', '222-222-2222')
    ]
    
    cursor.executemany(customerSQL, customerRecord)
    
    """Display all from customers table"""
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    
    print(" -- DISPLAYING ENTRIES FROM CUSTOMER TABLE -- \n\n")
    for customer in customers:
        print(customer)
        print("\n")
    
    
    """Executemany values into employees table"""
    employeeSQL = "INSERT INTO employees(f_name, l_name, date_of_birth, title, supervisor_id) VALUES (%s, %s, %s, %s, %s)"
    employeeRecord = [
        ('John', 'MacNell', datetime(1990, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Guide', 6),
        ('D.B', 'Marland', datetime(1991, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Guide', 6),
        ('Anita', 'Gallegos', datetime(1992, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Marketing', 7),
        ('Dimitrios', 'Stravopolous', datetime(1993, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Inventory Manager', 7),
        ('Mei', 'Wong', datetime(1994, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Marketing', 6),
        ('Blythe', 'Fletcher', datetime(1989, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Boss', 7),
        ('Jim', 'Fletcher', datetime(1988, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'), 'Co-Boss', 6),
    ]
    
    cursor.executemany(employeeSQL, employeeRecord)
    
    """Display all from customers table"""
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM EMPLOYEE TABLE -- \n\n")
    for employee in employees:
        print(employee)
        print("\n")
    
    
    """Executemany values into trek table"""
    trekSQL = "INSERT INTO trek(trek_name, country, requires_visa, required_immunizations) VALUES (%s, %s, %s, %s)"
    trekRecord = [
        ('Tanzania', 'Africa', 1, 1),
        ('Thailand', 'Asia', 1, 1),
        ('Ghana', 'Africa', 1, 1),
        ('Rome', 'Southern Europe', 1, 0),
        ('Hunan', 'Asia', 1, 1),
    ]
    
    cursor.executemany(trekSQL, trekRecord)
    
    """Display all from trek table"""
    cursor.execute("SELECT * FROM trek")
    treks = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM TREK TABLE -- \n\n")
    for trek in treks:
        print(trek)
        print("\n")
    

    """Executemany values into trek_history table"""
    trekHistorySQL = "INSERT INTO trek_history(customer_id, trek_id, trip_cost, trip_date) VALUES (%s, %s, %s, %s)"
    trekHistoryRecord = [
        (1, 1, 1000, datetime(2020, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (2, 1, 1000, datetime(2020, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (2, 2, 850, datetime(2020, 2, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (3, 3, 1000, datetime(2020, 3, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (4, 4, 750, datetime(2020, 4, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (5, 5, 850, datetime(2020, 4, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (6, 4, 750, datetime(2020, 4, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (5, 3, 1000, datetime(2020, 5, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (2, 3, 1000, datetime(2020, 5, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (6, 3, 850, datetime(2020, 5, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'))
    ]
    
    cursor.executemany(trekHistorySQL, trekHistoryRecord)
    
    """Display all from trek_history table"""
    cursor.execute("SELECT * FROM trek_history")
    trek_history = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM TREK HISTORY TABLE -- \n\n")
    for trekHis in trek_history:
        print(trekHis)
        print("\n")
    
    
    """Executemany values into inventory table"""
    inventorySQL = "INSERT INTO inventory(gear_name, for_rent, purchase_date) VALUES (%s, %s, %s)"
    inventoryRecord = [
        ('Boots', 0, datetime(2013, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Lantern', 1, datetime(2018, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Tent', 1, datetime(2012, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Lighter', 0, datetime(2020, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Hydro Flasks', 1, datetime(2015, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Backpack', 1, datetime(2016, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Boots', 0, datetime(2019, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Lantern', 1, datetime(2018, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Tent', 1, datetime(2016, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Lighter', 0, datetime(2020, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Hydro Flasks', 1, datetime(2020, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        ('Backpack', 1, datetime(2013, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S'))
    ]
    
    cursor.executemany(inventorySQL, inventoryRecord)
    
    """Display all from inventory table"""
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()

    print("\n\n -- DISPLAYING ENTRIES FROM INVENTORY TABLE -- \n\n")
    for stock in inventory:
        print(stock)
        print("\n")

    """Executemany values into orders table"""
    orderSQL = "INSERT INTO orders(trek_history_id, order_date) VALUES (%s, %s)"
    orderRecord = [
        (1, datetime(2020, 1, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (2, datetime(2020, 2, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (3, datetime(2020, 3, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (4, datetime(2020, 4, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (5, datetime(2020, 5, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (6, datetime(2020, 6, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (8, datetime(2020, 6, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),
        (9, datetime(2020, 6, 10, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')),

    ]
    
    cursor.executemany(orderSQL, orderRecord)
    
    """Display all from orders table"""
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM ORDERS TABLE -- \n\n")
    for order in orders:
        print(order)
        print("\n")
    
    """Executemany values into order_details table"""
    orderSQL = "INSERT INTO order_details(order_id, gear_id, purchase_cost, rental_cost) VALUES (%s, %s, %s, %s)"
    rentals = [
        (1, 2, 0, 20),
        (1, 3, 0, 45),
        (1, 5, 0, 20),
        (1, 6, 0, 20),
        (2, 2, 0, 20),
        (2, 3, 0, 45),
        (2, 6, 0, 20),
        (3, 3, 0, 45),
        (4, 2, 0, 20),
        (4, 3, 0, 45),
        (4, 5, 0, 20),
        (4, 6, 0, 20),
        (7, 2, 0, 20),
        (7, 3, 0, 45),
        (7, 5, 0, 20),
        (7, 6, 0, 20),
        (8, 2, 0, 20),
        (8, 3, 0, 45),
        (8, 5, 0, 20),
        (8, 6, 0, 20),
        (1, 1, 60, 0),
        (1, 4, 45, 0),
        (2, 7, 60, 0),
        (2, 10, 5, 0),
        (2, 11, 40, 0),
        (2, 1, 45, 0),
        (3, 6, 60, 0),
        (3, 8, 40, 0),
        (3, 10, 5, 0),
        (3, 11, 40, 0),
        (3, 12, 45, 0),
        (4, 1, 60, 0),
        (6, 7, 60, 0),
        (6, 8, 40, 0),
        (6, 9, 150, 0),
        (6, 10, 5, 0),
        (6, 11, 40, 0),
        (6, 12, 45, 0),
    ]
    
    cursor.executemany(orderSQL, rentals)
    
    """Display all from order_details table"""
    cursor.execute("SELECT * FROM order_details")
    orderDetails = cursor.fetchall()

    print("\n\n -- DISPLAYING ENTRIES FROM CUSTOMER_RENTALS TABLE -- \n\n")
    for order in orderDetails:
        print(order)
        print("\n")

    """Executemany values into employee_trek_history table"""
    empTrekSQL = "INSERT INTO employee_trek_history(trek_history_id, employee_id, supervisor_id) VALUES (%s, %s, %s)"
    empTrekRecord = [
        (1, 1, 6),
        (2, 2, 6),
        (3, 1, 6),
        (4, 1, 7),
        (5, 2, 7),
        (6, 1, 6)
    ]
    
    cursor.executemany(empTrekSQL, empTrekRecord)
    
    """Display all from employee_trek_history table"""
    cursor.execute("SELECT * FROM employee_trek_history")
    empTrek = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM EMPLOYEE TREK HISTORY TABLE -- \n\n")
    for history in empTrek:
        print(history)
        print("\n")
    
    
    
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
    