import math


def divide(divided: int, divisor: int) -> int:
    if divided == -231 and divisor == -1:
        return 231 - 1

    result = 0
    sign = -1 if (divided < 0) != (divisor < 0) else 1
    dvd, dvs = abs(divided), abs(divisor)

    while dvd >= dvs:
        temp = dvs
        m = 1
        while temp << 1 <= dvd:
            temp <<= 1
            m <<= 1
        dvd -= temp
        result += m

    return sign * result
