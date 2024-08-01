def Console(Input: str) -> str:
    Commands = ["exit", "help", "info", "list", "tools"]
    Input = Input.split()
    match Input[0].lower():
        case "exit":
            Command = 0
        case "help":
            Command = 1
        case "info":
            Command = 2
        case "ls":
            Command = 3
        case "list":
            Command = 3
        case "quit":
            Command = 0
        case "tools":
            Command = 4
        case _:
            print("Command not found:", Input[0])

    try: # Command not found
        Command = Commands[Command]
    except:
        Command = None
    
    try: # Skip argument for commands with no argument
        Argument = Input[1]
    except:
        Argument = None
    
    Text = [Command, Argument]
    return Text