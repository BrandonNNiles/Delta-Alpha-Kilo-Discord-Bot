import discord
from discord.ext import commands
from config import *
from SQLite import *
from console import *
import time
import aioconsole

client = commands.Bot(command_prefix = ',')
DAKServerID = 275482449591402496

#Methods

async def commandListener():
    while True:
        attempt = await aioconsole.ainput("Enter a command: ")
        executeCommand(attempt.lower())



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
    print("{}".format(message.author.guild.id))
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

'''
    A list of commands to be available to command line.
'''

from console import *


Command(help_id, 
        "Displays all commands available.",
        cmdHelp)


def cmdPrint(id = None):
    if id is None:
        print("Please specifiy a command.")
    else:
        print(executeCommand(command_prefix + id))

Command("print",
        "Prints the result of executing a given command.",
        cmdPrint,
        ["Command"]
)

def cmdSay(channelID, message):
    print("Placeholder")

Command("say",
        "Sends a message to a given channel.",
        cmdSay,
        ["ChannelID", "Message"]
)

def cmdChannelList(guildID):
    guild = client.get_guild(int(guildID[0]))
    channels = guild.text_channels
    print("Found {} channels in {}:".format(len(channels), guild.name))
    for channel in guild.text_channels:
        print("{}: {}".format(channel.name, channel.id))

Command("channellist",
        "Prints a list of all channels and their IDs.",
        cmdChannelList,
        ["GuildID"]
)

def cmdGuildList():
    print("Found {} guilds.".format(len(client.guilds)))
    for guild in client.guilds:
        print("{}: {}".format(guild.name, guild.id))

Command("guildlist",
        "Prints a list of guilds and IDs that the bot is in.",
        cmdGuildList
)

####################
#Your commands below
####################

'''
Command("name",
        "Description.",
        function,
        ["Argument1", "Argument2", "ArgumentX"]
)
'''

bot_token = open(token_file, "r").read() #Work on encryption later
startBot(bot_token) #Must be last line