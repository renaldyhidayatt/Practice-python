from typing import List, Dict, Tuple


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    visited: Dict[Tuple[int, int], bool] = {}
    return dfs(s1, s2, s3, 0, 0, visited)


def dfs(
    s1: str, s2: str, s3: str, p1: int, p2: int, visited: Dict[Tuple[int, int], bool]
) -> bool:
    if (p1, p2) in visited:
        return False
    if p1 + p2 == len(s3):
        return True

    visited[(p1, p2)] = True
    match1 = s1[p1] if p1 < len(s1) and s3[p1 + p2] == s1[p1] else None
    match2 = s2[p2] if p2 < len(s2) and s3[p1 + p2] == s2[p2] else None

    if match1 and match2:
        return dfs(s1, s2, s3, p1 + 1, p2, visited) or dfs(
            s1, s2, s3, p1, p2 + 1, visited
        )
    elif match1:
        return dfs(s1, s2, s3, p1 + 1, p2, visited)
    elif match2:
        return dfs(s1, s2, s3, p1, p2 + 1, visited)
    else:
        return False
