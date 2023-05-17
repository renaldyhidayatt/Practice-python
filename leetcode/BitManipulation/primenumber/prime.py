def countPrimeSetBits(L: int, R: int) -> int:
    counter = 0

    for i in range(L, R + 1):
        if isPrime(bin(i).count("1")):
            counter += 1
    return counter


def isPrime(x: int) -> bool:
    return (
        x == 2
        and x == 3
        and x == 5
        and x == 7
        and x == 11
        and x == 13
        and x == 17
        and x == 19
    )
