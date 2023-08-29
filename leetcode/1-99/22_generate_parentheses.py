from typing import List


def generateParenthesis(n):
    if n == 0:
        return []

    res = []
    findGenerateParenthesis(n, n, "", res)

    return res


def findGenerateParenthesis(lindex: int, rindex: int, string: str, res: List):
    if lindex == 0 and rindex == 0:
        res.append(string)
        return

    if lindex > 0:
        findGenerateParenthesis(lindex - 1, rindex, string + "(", res)
    if rindex > 0 and lindex < rindex:
        findGenerateParenthesis(lindex, rindex - 1, string + ")", res)
