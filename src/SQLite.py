'''
    SQLite.py
    Purpose:
        Uses SQLite3 to manage database related
'''

#Imports
import sqlite3
import os
from config import db_directory

#Methods

#Connects to a given database file
def openConn(filename):
    path = db_directory + str(filename) + ".db"
    conn = sqlite3.connect(path)
    c = conn.cursor()
    return conn, c

#Closses a connection
def closeConn(conn):
    conn.commit()
    conn.close()

#Creates default tables for a given file
def createTables(fileID):

    conn, c = openConn(fileID)
    c.execute("""CREATE TABLE IF NOT EXISTS messages(
        username text,
        user_id integer,
        message_text text,
        message_id integer,
        channel text,
        timestamp text
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS connect(
        username text,
        user_id integer,
        bot bool,
        invite text,
        invited_name text,
        invited_id integer,
        timestamp text
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS leave(
        username text,
        user_id integer,
        bot bool,
        timestamp text
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS stats(
        total_messages integer,
        total_members integer

    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS members(
        username text,
        user_id integer,
        voice_connections integer,
        chat_messages integer

    )""")
    closeConn(conn)

#Attempts to initialize the database
async def dbInit(guild):
    fileID = str(guild.id)
    os.chdir(os. getcwd())
    if not os.path.isdir(db_directory):   
        os.mkdir(db_directory)
    if not os.path.exists(db_directory + fileID + ".db"):
        print("Database for " + guild.name + " not found. Creating...")
        createTables(fileID)
        await transcribe(guild)
    print("Database for " + fileID +" initialized successfully.")

#Attempts to log a a given message to a given file
def logMessage(fileID, message):
    conn, c = openConn(fileID)
    username = message.author.name
    user_id = message.author.id
    message_text = message.content
    message_id = message.id
    channel = message.channel.name
    timestamp = message.created_at #times are in UTC and must be converted
    c.execute("INSERT INTO messages VALUES (?,?,?,?,?,?)",
    (username, user_id, message_text, message_id, channel, timestamp))
    closeConn(conn)

#Attempts to log a new member event to a given file
def logJoin(fileID, user, invite):
    conn, c = openConn(fileID)
    username = user.name
    user_id = user.id
    bot = user.bot
    invite = invite.code
    invited_name = invite.inviter.name
    invited_id = invite.inviter.id
    timestamp = user.joined_at#times are in UTC and must be converted
    if timestamp == None:
        timestamp = "Unknown"
    c.execute("INSERT INTO connect VALUES (?,?,?,?,?,?, ?)",
    (username, user_id, bot, invite, invited_name, invited_id, timestamp))
    closeConn(conn)

#Attempts to log a member leaving event to a given file
def logLeave(fileID, user):
    conn, c = openConn(fileID)
    username = user.name
    user_id = user.id
    bot = user.bot
    timestamp = user.joined_at#times are in UTC and must be converted
    if timestamp == None:
        timestamp = "Unknown"
    c.execute("INSERT INTO leave VALUES (?,?,?,?)",
    (username, user_id, bot, timestamp))
    closeConn(conn)

def searchDB(fileID, phrase):
    phrase = '%' + phrase + '%'
    conn, c = openConn(fileID)
    c.execute("SELECT * from messages WHERE message_text LIKE (?)", (phrase,))
    items = c.fetchall()
    c.execute("SELECT * from messages")
    count = c.fetchall()
    return items, count


#Prints the database to console, unformatted
def printDB(fileID):
    conn, c = openConn(fileID)
    c.execute("SELECT rowid, * FROM messages")
    print(c.fetchall())
    closeConn(conn)

#Logs all messages found in available channels in a given server
async def transcribe(guild):
    guildID = guild.id
    message_count = 0
    for channel in guild.text_channels:
        messages = channel.history(limit = None, before = None, after = None, around = None, oldest_first = True)
        async for message in messages:
            message_count = message_count + 1
            print("Logging message ({}) - {}".format(message_count, guild.name))
            logMessage(guildID, message)
    print("Transcription of {} complete.".format(guild.name))
    print("Logged {} messages.".format(message_count))
