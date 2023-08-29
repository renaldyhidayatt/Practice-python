from typing import List

letter_map = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def letterCombinations(digits: str) -> List[int]:
    res = []

    def findCombination(digits: str, index: int, s: str):
        if index == len(digits):
            res.append(s)
            return

        num = digits[index]
        letters = letter_map[int(num)]

        for letter in letters:
            findCombination(digits, index + 1, s + letter)

    if digits:
        findCombination(digits, 0, "")

    return res
