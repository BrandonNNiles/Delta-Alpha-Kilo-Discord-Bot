'''
    A list of commands to be available to command line.
'''
from console import *

class CommandSender():
    client = None
    def __init__(self, client):
        self.__class__.client = client

#Creates text into a fixed length string
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

async def cmdGuildList():
    print("Found {} guilds.".format(len(CommandSender.client.guilds)))
    for guild in CommandSender.client.guilds:
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