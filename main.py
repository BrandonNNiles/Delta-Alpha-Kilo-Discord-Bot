import discord
from discord.ext import commands
from config import *
from SQLite import *

client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print("Bot initialized.")

def startBot(token):
    print("Attempting to start bot...")
    client.run(token)

bot_token = open(token_file, "r").read() #Work on encryption later
startBot(bot_token) #Must be last line
