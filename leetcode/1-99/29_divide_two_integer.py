import math


def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647

    result = 0
    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1

    dvd, dvs = abs(dividend), abs(divisor)

    while dvd >= dvs:
        temp = dvs

        m = 1

        while (temp << 1) <= dvd:
            temp <<= 1
            m <<= 1

        dvd -= temp

        result += m

    return sign * result
