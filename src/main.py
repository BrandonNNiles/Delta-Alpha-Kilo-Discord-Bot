import discord
from discord.ext import commands
import time
import os.path
import json

from config import bot_prefix, token_file
from SQLite import logMessage
from console import *
from commandfuncs import *
from events import *

client = commands.Bot(command_prefix = bot_prefix)
DAKServerID = 275482449591402496

#Methods

#Opens and returns the token specified
def getToken(filename):
    if not os.path.exists(filename):
        print(filename + " generated.")
        f = open(filename, "w")
        f.write("{\n    \"bot_token\": \"\"\n}")

    f = open(filename)

    bot_token = json.load(f)['bot_token']
    return bot_token

#Connects the client to the server
def startBot():
    print("Attempting to start bot...")
    token = getToken(token_file)
    if token == "":
        print("Error: Bot token not specified in " + token_file)
        return
    CommandSender(client)
    client.run(token)

#Attempts to log the entire history of a specified server.
#Call using: await logAll(DAKServerID)
# to do: move to a different file (commands ideally)
async def logAll(guildID, glimit = None, gbefore = None, gafter = None, garound = None, goldest_first = True):
    message_count = 0
    start = time.time()
    guild = client.get_guild(guildID)
    for channel in guild.text_channels:
        messages = channel.history(limit = glimit, before = gbefore, after = gafter, around = garound, oldest_first = goldest_first)
        async for message in messages:
            message_count = message_count + 1
            print("Logging message ({})".format(message_count))
            logMessage(guildID, message)
    finish = time.time()
    print("Backup complete.")
    time_elapsed = round(finish - start)
    print("Logged {} messages. Took {} seconds".format(message_count, time_elapsed))

#Events (see events.py)

@client.event
async def on_ready():
    events.ready()

@client.event
async def on_message(message):
    events.message(message)

@client.event
async def on_member_join(member):
    events.memberJoin(member)

@client.event
async def on_member_leave(member):
    events.memberLeave(member)

@client.event
async def on_disconnect():
    events.botDisconnect()

@client.event
async def on_message_delete(message):
    events.messageDeleted(message)

@client.event
async def on_bulk_message_delete(messages):
    for message in messages:
        events.messageDeleted(message)

@client.event
async def on_message_edit(before, after):
    events.messageEdit(before, after)


################
# Driver Code
################
startBot() #Must be last line