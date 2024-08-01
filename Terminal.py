from Shell.Console import Console
from Shell.Controller import Controller

class Drzewo:
    def __init__(self):
        self.Path = None
        self.Loop()
    
    def Loop(self):
        while True:
            Input = str(input("> "))
            Sanitized = Console(Input)
            Controller(Sanitized[0], Sanitized[1]) # Command and argument

Drzewo()
