'''
    Basic console command implementation to provide
    an interface with backend methods.
'''

#Configurables
#=============#

command_prefix = "/" #The prefix for typing commands, default: "/"
help_id = "help" #The command id for the help command, default: "help"

'''
    =================================
    Do not modify anything below here
    =================================
'''

#Command class definition
class Command:
    command_list = []
    def __init__(self, id, description, func, args = [None]):
        self.__class__.command_list.append(self)
        self.id = id #string: a unique name
        self.description = description #string: a description, only used for help command
        self.func = func #function: code to be executed
        self.args = args #a list of arguments to be provided, only used for help command

#Attempts to execute the function of a given command
def executeCommand(message):
    print()
    prefix = message[0]
    message = message[1:].split()
    id = message[0]

    args = None

    if len(message) > 1:
        args = message[1:] #if arguments exist

    found = False
    for command in Command.command_list:
        if command.id.lower() == id:
            found = True
            if args and command.args != [None]:
                return command.func(args) #args are always passed as a list of args
            else:
                return command.func()
    
    if not found:
        print("Unknown command, type {}{} for a list of commands.".format(command_prefix, help_id))

#Creates text into a fixed length string
def f_len(text, length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * (length - len(text)))
    return text

#Help command, displays a formated list of all commands
def cmdHelp():
    #header
    print("Found {} commands:\n".format(len(Command.command_list)))
    print("Command          Arguments                      Description")
    print("-------          ---------                      -----------")

    #body
    for command in Command.command_list:
        #args formatting
        if command.args[0] == None:
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
