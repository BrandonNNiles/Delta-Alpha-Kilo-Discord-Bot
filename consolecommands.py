'''
    A list of commands to be available to command line.
'''

from console import *


Command(help_id, 
        "Displays all commands available.",
        cmdHelp)

Command("quit",
        "Exits the command loop.",
        lambda: True
)

Command("f_quit",
        "Force terminates the command loop.",
        lambda: False
)

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

####################
#Example commands
####################

'''
Command("example_cap",
        "Capitalizes a string",
        lambda x: print(' '.join(x).upper()),
        ["String"]
)
'''

'''
def cmdHello():
    print("Hello world!")

Command("example_hello",
        "Says a greeting.",
        cmdHello
)
'''

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