def lengthOfLastWord(s: str) -> int:
    last = len(s) - 1

    while last >= 0 and s[last] == "":
        last -= 1

    if last < 0:
        return 0

    first = last

    while first >= 0 and s[first] != "":
        first -= 1

    return last - first
