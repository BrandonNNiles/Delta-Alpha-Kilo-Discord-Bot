import discord
from discord.ext import commands
from config import *
from SQLite import *
import time
from console import *
from commandfuncs import *

client = commands.Bot(command_prefix = ',')
DAKServerID = 275482449591402496

#Methods

#Connects the client to the server
def startBot(token):
    CommandSender(client)
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

#Tries to find needle code in haystack
def hasInvite(inviteList, code):
    correct_invite = None
    for invite in inviteList:
        if invite.code == code:
            correct_invite = invite
    return correct_invite()

#Determines an invite used by an individual when joining the server
async def getInvite(guildID):
    pre_invites = invites[guildID] #Check before and after
    post_invites = await client.get_guild(guildID).invites()
    correct_invite = None

    for invite in pre_invites:
        if invite.uses < hasInvite(post_invites, invite.code).uses:
            correct_invite = invite
    return invite

def messageDeleted(message):
    channel = message.channel
    author = message.author
    content = message.content
    print("A message by {} was deleted in {}: {}".format(author, channel, content))
    #log event placeholder

#Events

@client.event
async def on_ready():
    
    start = time.time()
    print("Bot initialized.")
    await commandListener()

@client.event
async def on_message(message):
    username = message.author.name
    content = message.content
    channel = message.channel.name
    print("[{}] {}: {}".format(channel, username, content))
    guildID = message.guild.id
    logMessage(guildID, message)

@client.event
async def on_member_join(member):
    username = member.name
    guildID = member.guild.id
    invite = getInvite(guildID)
    if invite == None:
        print("{} has joined from an unknown source.".format(username))
    else:
        inviteid = invite.code
        inviter = invite.inviter.name
        print("{} has joined from invite {} by {}".format(username, inviteid, inviter))
        logJoin(guildID, member, invite)

@client.event
async def on_member_leave(member):
    username = member.name
    guildID = member.guild.id
    invite = getInvite(guildID)
    print("{} has left the server".format(username))
    logLeave(guildID, member)

@client.event
async def on_disconnect():
    print("\n\nClient has lost connection to discord!\n\n")

@client.event
async def on_message_delete(message):
    messageDeleted(message)

@client.event
async def on_bulk_message_delete(messages):
    for message in messages:
        messageDeleted(message)

@client.event
async def on_message_edit(before, after):
    oldContent = before.content
    newContent = after.content
    author = before.author
    channel = before.channel
    print("{} edited message in {}:".format(author, channel))
    print("\t{}\n->\n\t{}".format(oldContent, newContent))
    #log event placeholder

bot_token = open(token_file, "r").read() #Work on encryption later
startBot(bot_token) #Must be last line