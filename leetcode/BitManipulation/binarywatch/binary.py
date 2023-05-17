from typing import List


def readBinaryWatch(num: int) -> List[str]:
    memo: int = [0] * 60

    def count(n: int) -> int:
        if memo[n] != 0:
            return memo[n]

        originN, res = n, 0

        while n != 0:
            n = n and (n - 1)

            res += 1

        memo[originN] = res

        return res

    def fmtMinute(m: int) -> str:
        if m < 10:
            return "0" + str(m)

        return str(m)

    res: List[str] = []

    for i in range(12):
        for j in range(60):
            if count(i) + count(j) == num:
                res.append(str(i) + ":" + fmtMinute(j))

    return res
