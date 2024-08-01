from Shell.Help import Help
from Shell.Exit import Exit
from Shell.Tools import Tools

def Controller(Command: str, Argument: str):
    match Command:
        case "exit":
            Exit()
        case "help":
            Help()
        case "tools":
            Tools()
