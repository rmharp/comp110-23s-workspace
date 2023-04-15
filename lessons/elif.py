SECRET: int = 11

if SECRET == 10:
    print("Correct!")
elif SECRET < 10:
        print("Your guess was too low.")
elif SECRET % 2 != 0:
    print("Your guess should be even and is too high.")
else:
        print("Your guess was too high.") 