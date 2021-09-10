import sqlite3
import os

db_directory = "db/"

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
def dbInit(fileID):
    print("Attempting to start database...")
    os.chdir(os. getcwd())
    if not os.path.isdir(db_directory):   
        os.mkdir(db_directory)
    createTables(fileID)
    print("Database initialized successfully.")

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

#Prints the database to console, unformatted
def printDB(fileID):
    conn, c = openConn(fileID)
    c.execute("SELECT rowid, * FROM messages")
    print(c.fetchall())
    closeConn(conn)

guildID = 275482449591402496
dbInit(guildID)