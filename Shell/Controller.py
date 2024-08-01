from Shell.Help import Help
from Shell.Exit import Exit

def Controller(Command: str, Argument: str):
    match Command:
        case "exit":
            Exit()
        case "help":
            Help()
