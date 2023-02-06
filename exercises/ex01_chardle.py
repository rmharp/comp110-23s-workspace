"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730470865"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chr: str = input("Enter a single character: ")
if len(chr) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + chr + " in " + word)

x: int = 0
if chr == word[0]:
    print(chr + " found at index 0")
    x = x + 1
if chr == word[1]:
    print(chr + " found at index 1")
    x = x + 1
if chr == word[2]:
    print(chr + " found at index 2")
    x = x + 1
if chr == word[3]:
    print(chr + " found at index 3")
    x = x + 1    
if chr == word[4]:
    print(chr + " found at index 4")
    x = x + 1

if x == 0:
    print("No instances of " + chr + " found in " + word)
if x == 1:
    print(str(x) + " instance of " + chr + " found in " + word)
if x > 1:
    print(str(x) + " instances of " + chr + " found in " + word)