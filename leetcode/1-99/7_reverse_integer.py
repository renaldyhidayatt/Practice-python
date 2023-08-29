def reverse(x: int) -> int:
    tmp = 0
    sign = 1 if x >= 0 else -1

    x = abs(x)

    while x != 0:
        tmp = tmp * 10 + x % 10
        x = x // 10

    if tmp > (1 << 31) - 1 or tmp < -(1 << 31):
        return 0

    return tmp * sign


print(reverse(123))
