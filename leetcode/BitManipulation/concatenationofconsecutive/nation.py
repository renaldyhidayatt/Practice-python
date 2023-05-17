def concatenatedBinarry(n: int) -> int:
    res, mod, shift = 0, 1000000007, 0

    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:
            shift += 1
        res = ((res << shift) + i) % mod
    return res
