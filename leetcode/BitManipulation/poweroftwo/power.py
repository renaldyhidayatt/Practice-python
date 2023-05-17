def isPowerOfTwo(num: int) -> bool:
    while num >= 2:
        if num % 2 == 0:
            num = num / 2
        else:
            return False

    return num == 1
