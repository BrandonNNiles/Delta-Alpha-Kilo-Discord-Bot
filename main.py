import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print("Bot initialized.")

client.run('ODg1MzUyNjYxNDkzMzY2ODI0.YTly6w.QkMXYOQDdMyavb647W2gRh-oqzI')
