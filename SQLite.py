import sqlite3
import os

db_directory = "db/"

def openConn(filename):
    path = db_directory + str(filename) + ".db"
    conn = sqlite3.connect(path)
    c = conn.cursor()
    return conn, c

def closeConn(conn):
    conn.commit()
    conn.close()

def createTables(fileID):
    #Create a Table
    conn, c = openConn(fileID)
    c.execute("""CREATE TABLE IF NOT EXISTS messages(
        username text,
        user_id integer,
        message_text text,
        message_id integer,
        channel text,
        timestamp text
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS join(
        username text,
        user_id integer,
        bot bool,
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
    closeConn(conn)

def dbInit(fileID):
    os.chdir(os. getcwd())
    if not os.path.isdir(db_directory):   
        os.mkdir(db_directory)
    createTables(fileID)
    print("Database initialized successfully.")

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

def logJoin(fileID, user, inviter):
    conn, c = openConn(fileID)
    username = user.name
    user_id = user.id
    bot = user.bot
    invited_name = inviter.name
    invited_id = inviter.id
    timestamp = user.joined_at#times are in UTC and must be converted
    if timestamp == None:
        timestamp = "Unknown"
    c.execute("INSERT INTO join VALUES (?,?,?,?,?,?)",
    (username, user_id, bot, invited_name, invited_id, timestamp))
    closeConn(conn)

def logLeave(fileID, user):
    conn, c = openConn(fileID)
    username = user.name
    user_id = user.id
    bot = user.bot
    timestamp = user.joined_at#times are in UTC and must be converted
    if timestamp == None:
        timestamp = "Unknown"
    c.execute("INSERT INTO leave VALUES (?,?,?,?,?,?)",
    (username, user_id, bot, timestamp))
    closeConn(conn)

def printDB(fileID):
    conn, c = openConn(fileID)
    c.execute("SELECT rowid, * FROM messages")
    print(c.fetchall())
    closeConn(conn)


print("Attempting to start database...")
guildID = 275482449591402496
dbInit(guildID)