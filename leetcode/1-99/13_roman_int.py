roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    if s == "":
        return 0

    num, lastInt, total = 0, 0, 0

    for i in range(len(s)):
        char = s[len(s) - (i + 1) : len(s) - i]
        num = roman[char]
        if num < lastInt:
            total = total - num
        else:
            total = total + num

        lastInt = num

    return total


print(romanToInt("LVIII"))
