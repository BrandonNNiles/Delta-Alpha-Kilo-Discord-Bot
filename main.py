import discord
from discord.ext import commands
from config import *
from SQLite import *
import time

client = commands.Bot(command_prefix = ',')
DAKServerID = 275482449591402496

#Methods

#Connects the client to the server
def startBot(token):
    print("Attempting to start bot...")
    client.run(token)

#Attempts to log the entire history of a specified server.
#Call using: await logAll(DAKServerID)
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

async def getInvite(guildID):
    pre_invites = invites[guildID]
    post_invites = await get_guild(guildID).invites()
    correct_invite = None

    for invite in pre_invites:
        if invite.uses < find_invite_by_code(post_invites, invite.code).uses:
            correct_invite = invite
    return invite

#Events

@client.event
async def on_ready():
    start = time.time()
    print("Bot initialized.")

@client.event
async def on_message(message):
    username = message.author.name
    content = message.content
    print("{}: {}".format(username, content))
    guildID = message.guild.id
    logMessage(guildID, message)

@client.event
async def on_member_join(member):
    username = member.name
    guildID = member.guild.id
    invite = getInvite(guildID)
    if invite == None:
        print("{} has joined from an unknown source.")
    else:
        inviteid = invite.code
        inviter = invite.inviter.name
        print("{} has joined from code {} by {}".format(username, inviteid, inviter))
        logJoin(guildID, member, invite)


bot_token = open(token_file, "r").read() #Work on encryption later
startBot(bot_token) #Must be last line