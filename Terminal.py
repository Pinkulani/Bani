from Console import Console

class Drzewo:
    def __init__(self):
        self.Path = None
        self.Loop()
    
    def Loop(self):
        while True:
            Input = str(input("> "))
            Console(Input)

Drzewo()