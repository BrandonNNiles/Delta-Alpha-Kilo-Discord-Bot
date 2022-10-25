'''
    console.py
    Purpose:
        Console command implementation to provide interface for backend methods.
'''

#Imports
import aioconsole
from config import help_id, console_prefix

#Command class definition
class Command:
    command_list = []
    def __init__(self, id, description, func, args = []):
        self.__class__.command_list.append(self)
        self.id = id #string: a unique name
        self.description = description #string: a description, only used for help command
        self.func = func #function: code to be executed
        self.args = args #a list of arguments to be provided, only used for help command
    def __lt__(self, other):
        return self.id < other.id

#This class is needed in order to get the client class from main, might be a different work around
class CommandSender():
    client = None
    chatMode = False #if true, all console input will be sent as chat messages to a previously defined channel
    chatChannel = None
    def __init__(self, client):
        self.__class__.client = client

#Override command input for console->discord channel chat
async def chatOverride(message):
    if message != console_prefix + "quit":
        message = [CommandSender.chatChannel, message]
        for command in Command.command_list:
            if command.id == "say":
                return await command.func(message)
        print("Chat command not found, disabling chat mode.") #this shouldn't happen
        CommandSender.chatMode = False
    else:
        print("Disabling chat mode.")
        CommandSender.chatMode = False
    return

#Attempts to execute the function of a given command
async def executeCommand(message):
    print()

    if CommandSender.chatMode: #Override rest of function, we are in chat mode now
        return await chatOverride(message)

    prefix = message[0]
    message = message[1:].split()
    id = message[0].lower()

    args = {}

    if len(message) > 1:
        args = message[1:] #if arguments exist

    found = False
    for command in Command.command_list:
        if command.id.lower() == id:
            found = True
            if len(args) >= len(command.args) and len(command.args):
                return await command.func(args) #args are always passed as a list of args
            elif (args == None and command.args != [None]) or (len(args) < len(command.args)): #args required but not given
                print("Missing {} arguments, required: {}".format(len(command.args) - len(args), command.args))
            else:
                return await command.func()
    
    if not found:
        print("Unknown command, type {}{} for a list of commands.".format(console_prefix, help_id))

#Loop to listen to user input via console
async def commandListener():
    while True:
        scanMessage = "Enter a command: "
        if CommandSender.chatMode:
            scanMessage = "D.A.K.: "
        attempt = await aioconsole.ainput(scanMessage)
        if attempt and attempt != "":
            await executeCommand(attempt)
