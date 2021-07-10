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

#Creating a select query to run after updates, insert, and deletes
def display_players(cursor, title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n -- {} --".format(title))
    for player in players:
        print(" Player ID: {} \n First name: {} \n Last name {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    #Query for player to be inserted
    add_player = ("INSERT INTO player (first_name, last_name, team_id)" "VALUES (%s, %s, %s)")

    #Add the new player to team 1
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)

    #commit to the DB
    db.commit()

    #Query for inner join (from queries file)
    display_players(cursor, "DISPLAY PLAYERS AFTER INSERT")
    
    #Update the record
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update_player)

    #Query for inner join (from queries file)
    display_players(cursor, "DISPLAY PLAYERS AFTER UPDATE")
    
    #commit to the DB
    db.commit()
    
    #Delete the record
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)

    #Query for inner join (from queries file)
    display_players(cursor, "DISPLAY PLAYERS AFTER DELETE")     

    #commit to the DB
    db.commit()

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
