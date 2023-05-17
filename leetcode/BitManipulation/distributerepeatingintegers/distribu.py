from typing import List, Dict


def canDistribute(nums: List[int], quantity: List[int]) -> bool:
    freq: Dict = {}

    for n in nums:
        freq[n] += 1

    return dfs(freq, quantity)


def dfs(freq: Dict, quantity: List[int]) -> bool:
    if len(quantity) == 0:
        return True

    visited: Dict = {}

    for i in freq:
        if freq[i] in visited:
            continue

        visited[freq[i]] = True

        if freq[i] >= quantity[0]:
            freq[i] -= quantity[0]
            if dfs(freq, quantity[1:]):
                return True
            freq[i] += quantity[0]

    return False
