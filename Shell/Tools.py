from String.Alphabet import Alphabet

def Tools():
    print("Tools")
    print("")
    Tools = ["Alphabet - Prints the alphabet with the position of the letter"]
    for Number, Tool in enumerate(Tools):
            print(str((Number + 1)) + ". " + Tool)
    while True:
        try: # Check for number
            Select = int(input("Select: "))
        except:
            try: # Check for exit
                Select = str(input("Select: "))
            except:
                print("Invalid input")
                continue

        match Select:
            case "exit":
                break
            case "quit":
                break
            case 1:
                Alphabet()