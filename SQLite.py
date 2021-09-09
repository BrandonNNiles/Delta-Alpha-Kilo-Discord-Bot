import sqlite3
import os
import time
import datetime

db_directory = "db"

def openConn():
    conn = sqlite3.connect('db/server_main.db')
    c = conn.cursor()
    return conn, c

def closeConn(conn):
    conn.commit()
    conn.close()

def createTables():
    #Create a Table
    conn, c = openConn()
    c.execute("""CREATE TABLE IF NOT EXISTS messages(
        username text,
        user_id integer,
        message_text text,
        message_id integer,
        channel text,
        timestamp text
    )""")
    closeConn(conn)

def dbInit():
    os.chdir(os. getcwd())
    if not os.path.isdir(db_directory):   
        os.mkdir(db_directory)
    createTables()
    print("Database initialized successfully.")


def logMessage(message):
    conn, c = openConn()
    username = message.author.name
    user_id = message.author.id
    message_text = message.content
    message_id = message.id
    channel = message.channel.name
    unix = time.time()
    timestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO messages VALUES (?,?,?,?,?,?)",
    (username, user_id, message_text, message_id, channel, timestamp))
    closeConn(conn)

def printDB():
    conn, c = openConn()
    c.execute("SELECT rowid, * FROM messages")
    print(c.fetchall())
    closeConn(conn)

print("Attempting to start database...")
dbInit()