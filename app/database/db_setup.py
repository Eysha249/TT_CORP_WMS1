from .db_connection import get_connection # go to the database db connection file and reuse the function get_connection

def create_tables(): #create database tables when the system starts
    connection = get_connection() #calls the imported function
    cursor = connection.cursor() #create cursor

    
    #database will create a table called users if one does not exit 

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users ( 
            user_id INTGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            usermane TEXT NOT NULL UNIQUE,
            password TECT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    connection.commit() # write inserts permanently to database file
    connection.close() # disconnects database

def insert_sample_users(): #put some example users into the database
    connection = get_connection() #call connection function sqlite3.connect ttcorp.db
    cursor = connection.cursor() # runs SQL Commands like insert/select/creat tabels

    #list that contains tuples for each column in the tabel to match fullname, username, password and role

    users = [
        ("Tom Becker","adm1becker1","admin123","Project Manager"),
        ("Eysha Howell","adm3howele","dev123","Developer"),
        ("Arshad Sher","adm3shere","dev1234","Developer")
                 
    ]

    for user in users:
        cursor.execute("""
            INSERT OR IGNOR INTO users (full_name, username,password, role)
            VALUES (?, ?, ?, ?)
        """, user)

    connection.commit()
    connection.close()




