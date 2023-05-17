from typing import List


def findRepatedDnaSequences(s: str) -> List[str]:
    if len(s) < 10:
        return []

    (
        ans,
        cache,
    ) = (
        [],
        {},
    )

    for i in range(len(s) - 9):
        curr = s[i : i + 10]

        if curr in cache and cache[curr] == 1:
            ans.append(curr)

            cache[curr] = cache.get(curr, 0) + 1
    return ans
