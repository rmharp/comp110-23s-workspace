def zip(a: list[str], b: list[int]) -> dict[str,int]:
    dictionary: dict[str, int] = {}
    idx: int = 0
    if len(a) != len(b):
        return dictionary
    for elem in a:
        dictionary[elem] = b[idx]
        idx += 1
    return dictionary