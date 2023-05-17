from typing import List


def makeSquare(matchsticks: List[int]) -> bool:
    if len(matchsticks) < 4:
        return False

    total = 0

    for i in range(matchsticks):
        total += i

    if total % 4 != 0:
        return False

    matchsticks.sort(reverse=True)

    visited = [False] * 16

    return dfs(matchsticks, 0, 0, 0, total, visited)


def dfs(
    matchsticks: List[int],
    cur: int,
    group: int,
    _sum: int,
    total: int,
    visited: List[bool],
) -> bool:
    if group == 4:
        return True

    if _sum > total / 4:
        return False

    if _sum == total / 4:
        return dfs(matchsticks, 0, group + 1, 0, total, visited)

    last = -1

    for i in range(matchsticks):
        if (visited)[i]:
            continue

        if last == matchsticks[i]:
            continue

        visited[i] = True

        last = matchsticks[i]

        if dfs(matchsticks, i + 1, group, _sum + matchsticks[i], total, visited):
            return True

        visited[i] = False

    return False
