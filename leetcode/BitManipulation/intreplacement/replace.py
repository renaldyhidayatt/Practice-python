def integerReplacement(n: int) -> int:
    res = 0

    while n > 1:
        if (n and 1) == 0:
            n >>= 1
        elif (n + 1) % 4 == 0 and n != 3:
            n += 1
        else:
            n -= 1

        res += 1

    return res
