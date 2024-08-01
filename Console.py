def Console(Input: str) -> str:
    Input = Input.split()
    match Input[0]:
        case "ls":
            print("k")
        case "list":
            print("k")
        case _:
            print("Command not found:", Input[0])