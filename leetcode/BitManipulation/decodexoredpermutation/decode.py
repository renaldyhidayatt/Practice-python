from typing import List


def decode(encoded: List[int]) -> List[int]:
    n, total, odd = len(encoded), 0, 0

    for i in range(1, n + 2):
        total ^= i

    for i in range(1, n, 2):
        odd ^= encoded[i]

    perm = [0] * (n + 1)
    perm[0] = total ^ odd

    for i, v in enumerate(encoded):
        perm[i + 1] = perm[i] ^ v

    return perm
