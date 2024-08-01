def LetterToNumber(Alphabet: str, Input: str) -> int:
    for Number, Letter in enumerate(Alphabet):
            if Input == Letter:
                return Number