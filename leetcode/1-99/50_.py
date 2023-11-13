def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        n = -n
        x = 1 / x
    tmp = my_pow(x, n // 2)

    if n % 2 == 0:
        return tmp * tmp

    return tmp * tmp * x
