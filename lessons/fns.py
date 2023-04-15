"""Practice with functions"""

def main():
    g(f("comp110"))

def f(x: str) -> int:
    return len(x) - 1

def g(x: int) -> bool:
    y: int = 10
    if x > y or (x % 2 == 0):
        print(f"{x} is large and/or even")
        return True
    else:
        return False

main()