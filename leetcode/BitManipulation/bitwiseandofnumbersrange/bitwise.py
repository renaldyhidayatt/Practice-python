def rangeBitwiseAnd(m: int, n: int) -> int:
    if m == 0:
        return 0

    moved = 0

    while m != n:
        m >>= 1
        n >>= 1
        moved += 1

    return m << int(moved)
