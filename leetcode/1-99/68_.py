def mySqrt(x: int) -> int:
    l, r = 0, x

    while l < r:
        mid = (l + r + 1) // 2
        if mid * mid > x:
            r = mid - 1

        else:
            l = mid

    return l
