"""EX02 - One-Shot-Wordle - Loops!"""

__author__ = "730470865"

word: str = input("What is your 6-letter guess? ")
secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_idx: int = 0

while len(word) != len(secret):
    word = input(f"That was not {len(secret)} letters! Try again: ")


if word[word_idx] == secret[word_idx]:
    a = GREEN_BOX
else:        
    while word_idx < len(secret):
        if word[word_idx] == secret[word_idx + 1]:
            a = YELLOW_BOX            
        else:
            word_idx = word_idx + 1
    word_idx = 1

if word[word_idx] == secret[word_idx]:
    b = GREEN_BOX
else:        
    while word_idx < len(secret):
        if word[word_idx] == secret[word_idx + 1]:
            b = YELLOW_BOX            
        else:
            word_idx = word_idx + 1
    word_idx = 2

if word[word_idx] == secret[word_idx]:
    c = GREEN_BOX
else:        
    while word_idx < len(secret):
        if word[word_idx] == secret[word_idx + 1]:
            c = YELLOW_BOX            
        else:
            word_idx = word_idx + 1
    word_idx = 3

if word[word_idx] == secret[word_idx]:
    d = GREEN_BOX
else:        
    while word_idx < len(secret):
        if word[word_idx] == secret[word_idx + 1]:
            d = YELLOW_BOX            
        else:
            word_idx = word_idx + 1
    word_idx = 4

if word[word_idx] == secret[word_idx]:
    e = GREEN_BOX
else:        
    while word_idx < len(secret):
        if word[word_idx] == secret[word_idx + 1]:
            e = YELLOW_BOX            
        else:
            word_idx = word_idx + 1
    word_idx = 5

if word[word_idx] == secret[word_idx]:
    f = GREEN_BOX
else:     
    while word_idx < len(secret):
        if word[word_idx] == secret[word_idx + 1]:
            f = YELLOW_BOX            
        else:
            word_idx = word_idx + 1
    word_idx = 5

if len(word) == 6:
    if word == secret:
        print(f"{a}{b}{c}{d}{e}{f}")
        print("Woo! You got it!")
    else:
        print(f"{a}{b}{c}{d}{e}{f}")
        print("Not quite. Play again soon!")