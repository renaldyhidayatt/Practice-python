def hammingWeight(num: int) -> int:
    count = 0

    while num != 0:
        num = num and (num - 1)

        count += 1

    return count
