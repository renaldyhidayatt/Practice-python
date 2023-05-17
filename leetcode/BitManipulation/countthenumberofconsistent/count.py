from typing import List


def countConsistenStrings(allowed: str, words: List[int]) -> int:
    allowedMap, res, flag = {}, 0, True
    for c in allowed:
        if c not in allowedMap:
            allowedMap[c] = 0
            allowedMap[c] += 1
        for word in words:
            flag = True
        for c in word:
            if c not in allowedMap:
                flag = False
                break
        if flag:
            res += 1
    return res
