"""EX05 - 'list' Utility Functions."""

__author__: "730470865"


def only_evens(input: list[int]) -> list[int]:
    """Returns only even integers from a given list (input)."""
    list_idx: int = 0
    alt_input: list[int] = []
    while list_idx < len(input):
        if input[list_idx] % 2 == 0:
            input_idx: list[int] = [input[list_idx]]
            alt_input += input_idx
        list_idx += 1
    return (alt_input)


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concates two lists (list1 and list2) into one list (list12)."""
    list12: list[int]
    list12 = list1 + list2
    return list12


def sub(input: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a subset for a specfied range (start_idx to end_idx) of a given list (input)."""
    alt_input: list[int] = []
    if start_idx < 0:
        start_idx = 0
    while start_idx < end_idx and start_idx < len(input):
        input_idx: list[int] = [input[start_idx]]
        alt_input += input_idx
        start_idx += 1
    return (alt_input)