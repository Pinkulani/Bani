from LetterToNumber import LetterToNumber

def Alphabet():
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for Letter in Alphabet:
        print("|", Letter, "|", LetterToNumber(Alphabet, Letter), "|" )