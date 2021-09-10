import discord
from discord.ext import commands
from config import *
from SQLite import *
import time

client = commands.Bot(command_prefix = ',')
DAKServerID = 275482449591402496

#Methods

def startBot(token):
    print("Attempting to start bot...")
    client.run(token)

async def logAll(guildID, glimit = None, gbefore = None, gafter = None, garound = None, goldest_first = True):
    message_count = 0
    start = time.time()
    guild = client.get_guild(guildID)
    for channel in guild.text_channels:
        messages = channel.history(limit = glimit, before = gbefore, after = gafter, around = garound, oldest_first = goldest_first)
        async for message in messages:
            message_count = message_count + 1
            print("Logging message ({})".format(message_count))
            logMessage(message)
    finish = time.time()
    print("Backup complete.")
    time_elapsed = round(finish - start)
    print("Logged {} messages. Took {} seconds".format(message_count, time_elapsed))


#Events

@client.event
async def on_ready():
    start = time.time()
    print("Bot initialized.")
    await logAll(DAKServerID)

@client.event
async def on_message(message):
    #print("Attempting to log message.")
    #logMessage(message)
    print()


bot_token = open(token_file, "r").read() #Work on encryption later
startBot(bot_token) #Must be last line