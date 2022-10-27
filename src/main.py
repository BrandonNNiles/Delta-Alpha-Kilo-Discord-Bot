'''
    main.py
    Purpose:
        Main bot handling executable.
'''

#Imports
import discord
from discord.ext import commands
import os.path
import json

from config import bot_prefix, token_file
from console import *
from commandfuncs import Command #Initializes all commands, find a better method
import events as events

client = commands.Bot(command_prefix = bot_prefix)

#Methods

#Opens and returns the token specified
def getToken(filename):
    if not os.path.exists(filename):
        print(filename + " generated.")
        f = open(filename, "w")
        f.write("{\n    \"bot_token\": \"YOUR_TOKEN_HERE\"\n}")

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

#Events (see events.py)

@client.event
async def on_ready():
    await events.ready()

@client.event
async def on_message(message):
    await events.message(message)

@client.event
async def on_member_join(member):
    await events.memberJoin(member, invites)

@client.event
async def on_member_leave(member):
    await events.memberLeave(member)

@client.event
async def on_disconnect():
    await events.botDisconnect()

@client.event
async def on_message_delete(message):
    await events.messageDeleted(message)

@client.event
async def on_bulk_message_delete(messages):
    for message in messages:
        await events.messageDeleted(message)

@client.event
async def on_message_edit(before, after):
    await events.messageEdit(before, after)

@client.event
async def on_guild_join(guild):
    await events.guildJoin(guild)


################
# Driver Code
################
startBot() #Must be last line