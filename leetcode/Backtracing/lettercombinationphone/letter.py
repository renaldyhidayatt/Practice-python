from typing import List


letterMap = [
    " ",  # 0
    "",  # 1
    "abc",  # 2
    "def",  # 3
    "ghi",  # 4
    "jkl",  # 5
    "mno",  # 6
    "pqrs",  # 7
    "tuv",  # 8
    "wxyz",  # 9
]
res: List[str] = []
final = 0


def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return List[str]

    res: List[str] = []

    findCombination(digits, 0, "")

    return res


def findCombination(digits: str, index: int, s: str):
    if index == len(digits):
        res.append(s)

        return
    num = digits[index]
    letter = letterMap[int(num)]

    for i in range(len(letter)):
        findCombination(digits, index + 1, s + letter[i])

    return
