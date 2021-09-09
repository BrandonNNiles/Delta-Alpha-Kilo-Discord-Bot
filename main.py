import discord
from discord.ext import commands
from config import *
from SQLite import *

client = commands.Bot(command_prefix = ',')

#Methods

def startBot(token):
    print("Attempting to start bot...")
    client.run(token)


#Events

@client.event
async def on_ready():
    print("Bot initialized.")

@client.event
async def on_message(message):
    print("Attempting to log message.")
    logMessage(message)

bot_token = open(token_file, "r").read() #Work on encryption later
startBot(bot_token) #Must be last line
