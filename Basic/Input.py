def Input(Message: str, Type: str):
    match Type:
        case "float":
            In = float(input(Message))
        case "int":
            In = int(input(Message))
        case "string":
            In = str(input(Message))
    
    return In