"""EX04 - 'list' Utility Functions"""

__author__ = "730470865"

def all(num_list: list, num: int) -> bool:
    contains_num: bool = True
    list_idx: int = 0
    while list_idx < len(num_list) and contains_num == True:
        if num_list[list_idx] == num:
            contains_num = True
        else:
            contains_num = False
        list_idx += 1
    return(contains_num)

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    max: int = input[list_idx]
    while list_idx < len(input):
        if input[list_idx] > max:
            max = input[list_idx]
        list_idx += 1
    return max


print(max([]))