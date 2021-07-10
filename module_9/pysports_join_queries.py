#Angela Perkins
#Module 9_2
#July 10, 2021

#Connect to DB (code from insert file)
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Angel@84",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}". format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue ...")
    cursor = db.cursor()

    #Query for inner join (new to assignment this week)
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #Get results and display results (code from queries file)
    players = cursor.fetchall()
    print("\n --DISPLAYING PLAYER RECORDS--")
    for player in players:
        print(" Player ID: {} \n First name: {} \n Last name {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    input("\n\n  Press any key to continue.")

#Handle DB exceptions (code from insert file)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_Error:
        print("The specified database does not exist")

    else:
        print(err)

#close DB
finally:
    db.close()
