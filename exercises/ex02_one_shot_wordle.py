"""EX02 - One-Shot-Wordle - Loops!"""

__author__ = "730470865"

word: str = input("What is your 6-letter guess? ")
secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0

while len(word) != 6:
    word = input("That was not 6 letters! Try again: ")

while index < len(secret):
    if word[index] == secret[index]:
        a = GREEN_BOX
        index = index + 1
    else:
        if word[index] == secret[index+1]:
            a = YELLOW_BOX
        else:
            if word[index] == secret[index+2]:
                a = YELLOW_BOX
            else:
                if word[index] == secret[index+3]:
                    a = YELLOW_BOX
                else:
                    if word[index] == secret[index+3]:
                        a = YELLOW_BOX
                    else:
                        if word[index] == secret[index+4]:
                            a = YELLOW_BOX
                        else:
                            if word[index] == secret[index+5]:
                                a = YELLOW_BOX
                            else:
                                a = WHITE_BOX
    if word[1] != secret[1]:
        b = WHITE_BOX
    else:
        b = GREEN_BOX
    if word[2] != secret[2]:
        c = WHITE_BOX
    else:
        c = GREEN_BOX
    if word[3] != secret[3]:
        d = WHITE_BOX
    else:
        d = GREEN_BOX
    if word[4] != secret[4]:
        e = WHITE_BOX
    else:
        e = GREEN_BOX
    if word[5] != secret[5]:
        f = WHITE_BOX
    else:
        f = GREEN_BOX

if len(word) == 6:
    if word == secret:
        print(f"{a}{b}{c}{d}{e}{f}")
        print("Woo! You got it!")
    else:
        print(f"{a}{b}{c}{d}{e}{f}")
        print("Not quite. Play again soon!")