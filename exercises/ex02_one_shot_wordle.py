"""EX02 - One-Shot-Wordle - Loops!"""

__author__ = "730470865"

word: str = input("What is your 6-letter guess? ")
secret: str = "apples"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_idx: int = 0
alt_idx: int = 0
result: str = ""
yellow: bool = False
green: bool = False

while len(word) != len(secret):
    word = input(f"That was not {len(secret)} letters! Try again: ")

while word_idx < len(word):
    if secret[word_idx] == word[word_idx]:
        result = result + GREEN_BOX
        green = True
    else:        
        while alt_idx < len(secret) and not yellow:
            if word[word_idx] == secret[alt_idx]:
                result = result + YELLOW_BOX
                yellow = True            
            else:
                alt_idx = alt_idx + 1
    if not yellow and not green:
        result = result + WHITE_BOX
    yellow = False
    green = False
    alt_idx = 0
    word_idx = word_idx + 1

if len(word) == 6:
    if word == secret:
        print(f"{result}")
        print("Woo! You got it!")
    else:
        print(f"{result}")
        print("Not quite. Play again soon!")