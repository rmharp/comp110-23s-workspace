"""EX07 - Dictionary Functions."""

__author__ = "730470865"


def invert(start: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary so that the keys become values and the values become keys."""
    result: dict[str, str] = {}
    value: str = ""
    for key in start:
        value = start[key]
        if value in result:
            raise KeyError("More than one of same key will occur in result.")
        result[value] = key
    return result


def favorite_color(names_fc: dict[str, str]) -> str:
    """Takes a dictionary of people assigned to their favorite color and counts the number of each color.
    
    Next, this function finds the color(s) with the highest number counted. 
    Finally, it returns only the first of the highest counted colors as the favorite color.
    """
    color_count: dict[str, int] = {}
    most_popular: int = 0
    idx: int = 0
    color: str = ""
    for name in names_fc:
        color = names_fc[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    for color in color_count:
        idx = color_count[color]
        if most_popular < idx:
            most_popular = idx
    for color in color_count:
        if color_count[color] == most_popular:
            return color
    return color


def count(list1: list[str]) -> dict[str, int]:
    """Counts the frequency of a string occuring in a given list and returns the string with it's corresponding number of occurences as a dictionary."""
    freq_count: dict[str, int] = {}
    for item in list1:
        if item in freq_count:
            freq_count[item] += 1
        else:
            freq_count[item] = 1
    return freq_count