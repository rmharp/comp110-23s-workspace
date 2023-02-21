"""EX03 - Structured Wordle"""

___author___ = "730470865"

def contains_char(word: str,word_chr: str) -> bool:
    assert len(word_chr) == 1
    word_idx: int = 0
    while word_idx < len(word):
        if word[word_idx] == word_chr:
            return True
        else:
            word_idx += 1
    return False

def emojified(word: str, secret: str) -> str:
    assert len(word) == len(secret)
    word_idx: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    yellow: bool = False
    while word_idx < len(word):
        if contains_char(secret, word[word_idx]) == True:
            if word[word_idx] == secret[word_idx]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        word_idx += 1
    return(result)

def input_guess(length: int) -> str:
    word: str = input(f"Enter a {length} character word: ")
    while len(word) != length:
        word = input(f"That wasn't {length} chars! Try again: ")
    return (word)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    length: int = len(secret)
    turn_num: int = 1
    while turn_num <= 6:
        print(f"=== Turn {turn_num}/6 ===")
        word: str = input_guess(length)
        print(emojified(word, secret))
        if word != secret:
            turn_num += 1
        else:
            print(f"You won in {turn_num}/6 turns!")
            exit()
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
        
    