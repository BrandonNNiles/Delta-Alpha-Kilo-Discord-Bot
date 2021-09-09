import sqlite3
import os
import time
import datetime

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

def logMessage(message):
    print("Logging message.")
    unix = time.time()
    timestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M%S'))
    username = message.author.name
    user_id = message.author.id
    message_text = message.content
    message_id = message.id
    c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)",
    (username, user_id, message_text, message_id, timestamp))
    conn.commit
    print("Message logged.")

conn = sqlite3.connect('db/server_main.db')
c = conn.cursor()

dbInit()