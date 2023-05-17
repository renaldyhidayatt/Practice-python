from typing import List


def maxProducts(words: List[str]) -> int:
    if words == None or len(words) == 0:
        return 0

    length, value, maxProduct = len(words), [0] * len(words), 0

    for i in range(length):
        tmp = words[i]
        value[i] = 0
        for j in range(len(tmp)):
            value[i] |= 1 << (ord(tmp[j]) - ord("a"))

    for i in range(length):
        for j in range(i + 1, length):
            if (value[i] & value[j]) == 0 and (
                len(words[i]) * len(words[j]) > maxProduct
            ):
                maxProduct = len(words[i]) * len(words[j])

    return maxProduct
