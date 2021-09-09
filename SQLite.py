import sqlite3
import os

db_directory = "db"

def dbInit():
    os.chdir(os. getcwd())
    if not os.path.isdir(db_directory):   
        os.mkdir(db_directory)
    createTables()

def createTables():
    #Create a Table
    c.execute("""CREATE TABLE if not exists messages (
        username text,
        user_id text,
        message_text text,
        message_id integer,
        timestamp text
    )""")

conn = sqlite3.connect('db/server_main.db')
c = conn.cursor()

dbInit()