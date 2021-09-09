import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ',')


print("Attempting to start bot...")
@client.event
async def on_ready():
    print("Bot initialized.")


token = open("token.txt", "r").read()
client.run(token)
