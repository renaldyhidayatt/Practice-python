from typing import List


def letterCasePermutation(S: str) -> List[str]:
    if len(S) == 0:
        return List[str]

    res, pos, c = [], [], []

    SS = S.lower()

    for i in range(len(SS)):
        if isLowerLetter(SS[i]):
            pos.append(i)

        for i in range(len(pos) + 1):
            findLetterCasePermutation(SS, pos, i, c, res)

    return res


def findLetterCasePermutation(
    s: str, pos: List[int], target: int, index: int, c: List[int], res: List[str]
):
    if len(c) == target:
        b = list(s)

        for v in c:
            b[pos[v]] = b[pos[v]].upper()

            res.append("".join(b))

            return
    for i in range(index, len(pos) - (target - len(c)) + 1):
        c.append(i)

        findLetterCasePermutation(s, pos, target, i + 1, c, res)
        c.pop()


def isLowerLetter(c: str) -> bool:
    return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z")
