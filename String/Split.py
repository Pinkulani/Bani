def Split(Input: str) -> str:
    Array = []
    New = []
    for X in range(len(Input)):
        if Input[X] == " ":
            Array.append(New)
            New = []
        else:
            New.append(Input[X])

    Array.append(New) # Append last letters without space
    return Array
