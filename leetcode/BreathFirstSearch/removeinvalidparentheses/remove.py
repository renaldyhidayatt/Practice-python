from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def backtrace(i, cur, lmoves, rmoves, score):
            nonlocal res, mp

            if lmoves < 0 or rmoves < 0 or score < 0 or score > maxScore:
                return

            if lmoves == 0 and rmoves == 0:
                if len(cur) == length:
                    if cur not in mp:
                        res.append(cur)
                        mp[cur] = 1
                    return

            if i == n:
                return

            if s[i] == "(":
                backtrace(i + 1, cur + "(", lmoves, rmoves, score + 1)
                backtrace(i + 1, cur, lmoves - 1, rmoves, score)
            elif s[i] == ")":
                backtrace(i + 1, cur + ")", lmoves, rmoves, score - 1)
                backtrace(i + 1, cur, lmoves, rmoves - 1, score)
            else:
                backtrace(i + 1, cur + s[i], lmoves, rmoves, score)

        res = []
        mp = {}
        n = len(s)
        lmoves, rmoves, lcnt, rcnt = 0, 0, 0, 0

        for c in s:
            if c == "(":
                lmoves += 1
                lcnt += 1
            elif c == ")":
                if lmoves != 0:
                    lmoves -= 1
                else:
                    rmoves += 1
                rcnt += 1

        length = n - lmoves - rmoves
        maxScore = min(lcnt, rcnt)

        backtrace(0, "", lmoves, rmoves, 0)

        return res

    def min(self, a, b):
        if a < b:
            return a
        return b
