import discord
from discord.ext import commands
from config import *

client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print("Bot initialized.")

def startBot(token):
    print("Attempting to start bot...")
    client.run(token)

token = open(token_file, "r").read() #Work on encryption later
startBot(token) #Must be last line
