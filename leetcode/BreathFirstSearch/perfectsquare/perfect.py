import math


def numSquares(n: int) -> int:
    if isPerfectSquare(n):
        return 1

    if checkAnswer(n):
        return 4

    for i in range(1, int(math.sqrt(n)) + 1):
        j = n - i * i

        if isPerfectSquare(j):
            return 2

    return 3


def isPerfectSquare(n: int) -> bool:
    sq = int(math.floor(math.sqrt(float(n))))

    return sq * sq == n


def checkAnswer(x: int) -> bool:
    while x % 4 == 0:
        x /= 4

    return x % 8 == 7
