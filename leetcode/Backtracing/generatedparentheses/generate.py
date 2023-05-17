from typing import List


def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return List[int]
    res: List[str] = []

    findGenerateParenthesis(n, n, "", res)

    return res


def findGenerateParenthesis(lindex: int, rindex: int, mystr: str, res: List[str]):
    if lindex == 0 and rindex == 0:
        res.append(str)

        return

    if lindex > 0:
        findGenerateParenthesis(lindex - 1, rindex, mystr + "(", res)

    if rindex > 0 and lindex < rindex:
        findGenerateParenthesis(lindex, rindex - 1, str + ")", res)
