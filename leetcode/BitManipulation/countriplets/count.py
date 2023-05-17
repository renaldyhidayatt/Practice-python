from typing import List


def countTriplets(arr: List[int]) -> int:
    prefix, num, count, total = [0] * len(arr), 0, 0, 0

    for i, v in enumerate(arr):
        num ^= v
        prefix[i] = num

    for i in range(len(prefix) - 1):
        for k in range(i + 1, len(prefix)):
            total = prefix[k]

            if i > 0:
                total ^= prefix[i - 1]

            if total == 0:
                count += k - i

    return count
