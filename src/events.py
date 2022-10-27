'''
    events.py
    Purpose:
        A module used for defining the methods executed when events are called.
        Event wrappers in main.py call methods in this file.
'''

#Imports
from SQLite import logMessage, logJoin, logLeave, dbInit
from console import commandListener, CommandSender

#Methods

async def ready():
    print("Bot initialized.")
    for guild in CommandSender.client.guilds:
        await dbInit(guild)
    await commandListener()

async def message(message):
    username = message.author.name
    content = message.content
    channel = message.channel.name
    print("[{}] {}: {}".format(channel, username, content))
    guildID = message.guild.id
    logMessage(guildID, message)

async def messageDeleted(message):
    channel = message.channel
    author = message.author
    content = message.content
    print("A message by {} was deleted in {}: {}".format(author, channel, content))
    #log event placeholder

async def memberJoin(member, invites):
    username = member.name
    guild = member.guild
    guildID = guild.id
    invite = getInvite(guild, invites)
    if invite == None:
        print("{} has joined from an unknown source.".format(username))
    else:
        inviteid = invite.code
        inviter = invite.inviter.name
        print("{} has joined from invite {} by {}".format(username, inviteid, inviter))
        logJoin(guildID, member, invite)

async def memberLeave(member):
    username = member.name
    guild = member.guild
    guildID = guild.id
    invite = getInvite(guild)
    print("{} has left the server".format(username))
    logLeave(guildID, member)

async def botDisconnect():
    print("\n\nClient has lost connection to discord!\n\n")

async def messageEdit(before, after):
    oldContent = before.content
    newContent = after.content
    author = before.author
    channel = before.channel
    print("{} edited message in {}:".format(author, channel))
    print("\t{}\n->\n\t{}".format(oldContent, newContent))
    #log event placeholder

################
# Helper methods
################

#Tries to find needle code in haystack
def hasInvite(inviteList, code):
    correct_invite = None
    for invite in inviteList:
        if invite.code == code:
            correct_invite = invite
    return correct_invite()

#Determines an invite used by an individual when joining the server
async def getInvite(guild, invites):
    pre_invites = invites[guild.ID] #Check before and after
    post_invites = await guild.invites()
    correct_invite = None

    for invite in pre_invites:
        if invite.uses < hasInvite(post_invites, invite.code).uses:
            correct_invite = invite
    return correct_invite