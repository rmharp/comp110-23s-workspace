"""Practicing for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
num: list[int] = [1, 2, 3]
dictionary: dict[str, int] = {}
idx: int = 0
 
for elem in pets:
    dictionary[elem] = num[idx]
    idx += 1

print(dictionary)