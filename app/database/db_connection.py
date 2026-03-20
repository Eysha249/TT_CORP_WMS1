import sqlite3 #import sqlite3

def get_connection():
    connection = sqlite3.connect("data/ttcorp.db") #open database connection and store in ttcorp.db
    return connection

