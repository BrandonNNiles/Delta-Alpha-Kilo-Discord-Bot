'''
    commandfuncs.py
    Purpose:
        Provides implementation of various commands for use in the command line.
'''

#Imports
from console import *
from SQLite import searchDB

#Methods

#Creates text into a fixed length string, helper
def f_len(text, length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * (length - len(text)))
    return text

#Help command, displays a formated list of all commands
async def cmdHelp():
    #header
    print("Found {} commands:\n".format(len(Command.command_list)))
    print("Command          Arguments                      Description")
    print("-------          ---------                      -----------")

    #body
    listCommands = Command.command_list
    listCommands.sort()
    for command in listCommands:
        #args formatting
        if not len(command.args):
            args = "[None]"
        else:
            args = "[" + command.args[0]
            for arg in command.args[1:]:
                args = args + " " + arg
            args = args + "]"

        row = []
        row.append(f_len(command_prefix, 1))
        row.append(f_len(command.id, 15))
        row.append(f_len(args, 30))
        row.append(f_len(command.description, 80))
        
        print("{}{} {} {}".format(*row))

Command(help_id, 
        "Displays all commands available.",
        cmdHelp)

#Sends a message to channel
async def cmdSay(args):
    await CommandSender.client.wait_until_ready() #make sure we can send a message
    channelID = args[0]
    message = " "
    message = message.join(args[1:])
    await CommandSender.client.get_channel(int(channelID)).send(message)

Command("say",
        "Sends a message to a given channel.",
        cmdSay,
        ["ChannelID", "Message"]
)

#Enables chat-only mode
async def cmdStartChatting(args):
    channelID = args[0]
    CommandSender.chatChannel = channelID
    CommandSender.chatMode = True
    channel = CommandSender.client.get_channel(channelID)
    print("Chat-mode started for channel {}. Type /quit to exit".format(channel))

Command("startchatting",
        "Enables constant chat mode.",
        cmdStartChatting,
        ["ChannelID"])

#Prints a list of text channels in a given guild
async def cmdChannelList(guildID):
    guild = CommandSender.client.get_guild(int(guildID[0]))
    channels = guild.text_channels
    print("Found {} channels in {}:".format(len(channels), guild.name))
    for channel in guild.text_channels:
        print("{}: {}".format(channel.name, channel.id))

Command("channellist",
        "Prints a list of all channels and their IDs.",
        cmdChannelList,
        ["GuildID"]
)

#Prints a list of guilds that the bot client is connected to
async def cmdGuildList():
    print("Found {} guilds.".format(len(CommandSender.client.guilds)))
    for guild in CommandSender.client.guilds:
        print("{}: {}".format(guild.name, guild.id))

Command("guildlist",
        "Prints a list of guilds and IDs that the bot is in.",
        cmdGuildList
)

async def cmdDBCount(args):
    phrase = " ".join(args)
    trueCount = 0
    for guild in CommandSender.client.guilds:
        guildid = guild.id
        result, totalMessages = searchDB(guildid, phrase)
        count = len(result)
        total = len(totalMessages)
        for message in result:
            trueCount = trueCount + message[2].lower().count(phrase)

        print("\"{}\" occurs {} times over {} messages, total messages: {} in {}.".format(phrase, trueCount, count, total, guild.name))

Command("dbcount",
        "Counts how many times a given string occurs in the database",
        cmdDBCount,
        ["Phrase"]
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