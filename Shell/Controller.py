from Shell.Help import Help

def Controller(Command: str, Argument: str):
    match Command:
        case "help":
            Help()