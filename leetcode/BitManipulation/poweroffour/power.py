def isPowerOfFour(num: int) -> bool:
    while num >= 4:
        if num % 4 == 0:
            num = num / 4
        else:
            return False

    return num == 1
