"""EX06 - 'list' Utility Functions."""

__author__ = "730470865"

from random import randint

points: int = 0
player: str = ""
choice2: bool = False
choice4: bool = True
path_of_1: bool = False
SINGULARITY: str = "\U0001F300"
first_time: bool = True
direction: str = ""


def main() -> None:
    """Role playing game with an end goal of containing the singularity which is devouring earth."""
    global points
    global first_time
    choice: str = input("\nDo you want to play the game?\n\n")
    choice = YN(choice)
    while choice == "Yes" or choice == "yes":
        global path_of_1
        greet()
        if not choice4:
            return
        print(f"\nIt's nice to meet you {player}. Now that we've become acquainted, I need your help to save the world! Of course, this is only if you'd like to help... Would you like to help?\n")
        q1: str = input("Take some time to think about it and don't feel the need to respond only with yes or no.\n\n")
        if q1 == "Yes" or q1 == "yes":
            print("\nWell then, let's get started!\n")
        elif q1 == "No" or q1 == "no":
            print("\nWell have a good rest of the last day of your life!\n")
            return
        else:
            print("\nWell you didn't say no, and this is the last day we can get to know each other more. So, come with me!\n")
        print("We're going to stop the singularity from devouring the earth!\n")
        nors()
        if direction == "North":
            points += 1
            print("\nPING... That's the sound of my barometer. As we approach our destination, it will continue to PING each time we get closer.\n")
            lorr()
            while not choice2:
                print("\nLet's try that again, we should really start going the right way if we want to get there in time.\n")
                lorr()
            print("\nThat was the right choice and we're headed in the right direction!\n")
        else:
            choice = input("\nThat wasn't the right direction but we can only go up from here, don't worry there's more than one way to save the world! Would you like to keep going on this path?\n\n")
            choice = YN(choice)
            if choice == "Yes" or choice == "yes":
                print("\nWell then, let's keep going!\n")
                lorr()
                while not choice2:
                    print("\nLet's try that again, we should really start going the right way if we want to get there in time.\n")
                    lorr()
                print("\nThat was the right choice and we're headed in the right direction again!")
                print("\nPING... That's the sound of my barometer. As we approach our destination, it will continue to PING each time we get closer.\n")
                path_of_1 = True
            else:
                choice = input("\nWould you like to quit?\n\n")
                choice = YN(choice)
                if choice == "No" or choice == "no":
                    points += 1
                    print("\nWonderful, we'll head back north instead. PING... That's the sound of my barometer. As we approach our destination, it will continue to PING each time we get closer.\n")
                    lorr()
                    while not choice2:
                        print("\nLet's try that again, we should really start going the right way if we want to get there in time.\n")
                        lorr()
                    print("\nThat was the right choice and we're headed in the right direction!\n")
                else:
                    return
        points = total_points(points)
        if SINGULARITY == "\U00000000":
            print(f"\nWe've reached the singularity by making a total of {points} correct turns! You should be feeling an intense gravitational pull towards it!\n")
        else:
            print(f"We've reached the singularity by making a total of {points} correct turns! You should be feeling an intense gravitational pull towards it!\n")
        print("The singularity feeds off of pressure and continues to create more singularities.\n")
        print("In order to counter act this, we'll need to create an environment that forces the singularity into an enclosure without access to additional matter.\n")
        print("Then we'll place a gravity pump into the center of the enclosure far enough away that the outer bounds cannot be damaged.\n")
        print("Give me a countdown to shutdown the singularity!\n")
        countdown()
        first_time = False
        print(f"\n{SINGULARITY}")
        choice = input("\nDo you want to play again?\n\n")
        choice = YN(choice)


def greet() -> None:
    """Function used to define a player name for the game."""
    global player
    global choice4
    player = input("\nHello Traveler, I hope you are well! Could you please tell me your name?\n\n")
    if player == "No" or player == "no":
        choice3: str = input("\nWould you like to quit?\n\n")
        while choice3 != "Yes" and choice3 != "yes" and choice3 != "No" and choice3 != "no":
            choice3 = input("\nI need a Yes or No answer.\n\n")
        if choice3 == "No" or choice3 == "no":
            player = input("\nWhat is your name?\n\n")
        else:
            choice4 = False


def nors() -> None:
    """Function used to determine North or South direction."""
    global direction
    length: int = int((input(f"Ok, {player} for our first task we'll need to choose whether to take the North or South path.\n\nThe only advice I've been given is to use the length of the traveler's name with whom I've ended up.\n\nHow long is your name?\n\n")))
    while len(player) != (length):
        length = int(input(f"\nAre you sure {player} is {length} letters long? When you're ready to proceed, let me know the correct length.\n\n"))
    NorthVar: int = 5
    Q2Response: str = input(f"\nIf the answer you gave me was longer than {NorthVar} then I'd recommend we go North, otherwise let's go South. Do you agree?\n\n")
    Q2Response = YN(Q2Response)
    if Q2Response == "Yes" and len(player) > NorthVar or Q2Response == "yes" and len(player) > NorthVar or Q2Response == "No" and len(player) <= NorthVar or Q2Response == "no" and len(player) <= NorthVar:
        direction = "North"
    if Q2Response == "Yes" and len(player) <= NorthVar or Q2Response == "yes" and len(player) <= NorthVar or Q2Response == "No" and len(player) > NorthVar or Q2Response == "no" and len(player) > NorthVar:
        direction == "South"


def lorr() -> None:
    """Function used to determine Left or Right direction with a coin toss."""
    heads: int = 1
    tails: int = 0
    global choice2
    global points
    choice2 = False
    print("Would you like to go left or right? Keep in mind the singularity is very devious and is constantly shifting around us. \n")
    Q4Response: str = input("Wait! I know how we'll decide, I'll flip a coin. Do you want the left path to be heads or tails?\n\n")
    while Q4Response != "Tails" and Q4Response != "tails" and Q4Response != "heads" and Q4Response != "Heads":
        Q4Response = input("Heads or tails? ")
    coin: int = 0
    coin += randint(0, 1)
    if coin == 1:
        print("\nThe coin landed on heads.")
    else:
        print("\nThe coin landed on tails.")
    if Q4Response == "heads" or Q4Response == "Heads":
        if coin == heads:
            points += 1
            choice2 = True
    else:
        if coin == tails:
            points += 1
            choice2 = True


def YN(response: str) -> str:
    """Function used to save space with the purpose of removing possible edge cases."""
    while response != "Yes" and response != "yes" and response != "No" and response != "no":
        response = input(f"\nI need a Yes or No answer, {player}.\n\n")
    return response


def countdown() -> None:
    """Function used to save space with the purpose of a countdown procedure."""
    idx: int = int(input())
    while idx > 1:
        num: int = int(input("\n"))
        while num >= idx:
            print(f"\nI need a correct sequence of numbers for this to be a proper countdown, {player}.\n")
            num = int(input("\nWhat's the next number in the sequence?\n\n"))
        idx -= 1


def total_points(x: int) -> int:
    """Function used to decide whether to include or exclude turns from previous games."""
    global first_time
    if first_time:
        return x
    include: str = input("Would you like to include turns from previous games in this instance of the game?\n\n")
    include = YN(include)
    if include == "yes" or include == "Yes":
        return x
    else:
        if path_of_1:
            x = 1
            return x
        else:
            x = 2
            return x


if __name__ == "__main__":
    main()