"""EX04 - 'list' Utility Functions."""

__author__ = "730470865"


def all(num_list: list[int], num: int) -> bool:
    """Checks if the  list (num_list) contains a number (num)."""
    contains_num: bool = True
    list_idx: int = 0
    if len(num_list) == 0:
        return False
    while list_idx < len(num_list) and contains_num:
        if num_list[list_idx] == num:
            contains_num = True
        else:
            contains_num = False
        list_idx += 1
    return (contains_num)


def max(input: list[int]) -> int:
    """Searches for the maximum integer of a list (input)."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    max: int = input[list_idx]
    while list_idx < len(input):
        if input[list_idx] > max:
            max = input[list_idx]
        list_idx += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if the  first (list1) and second (list2) lists are equal at each index."""
    is_equal: bool = True
    list_idx: int = 0
    if len(list1) != len(list2):
        return False
    while list_idx < len(list1):
        if list1[list_idx] != list2[list_idx]:
            is_equal = False
        list_idx += 1
    return is_equal