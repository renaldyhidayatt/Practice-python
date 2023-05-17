from typing import List
from collections import deque


def findOrder(numCourses: int, prerequisites: List[int]):
    in_degree = [0] * numCourses
    frees = [[] for _ in range(numCourses)]
    next_courses = deque()
    result = []

    for v in prerequisites:
        in_degree[v[0]] += 1

        frees[v[1]].append(v[0])

    for i in range(numCourses):
        if in_degree[i] == 0:
            next_courses.append(i)

    while next_courses:
        c = next_courses.popleft()
        v = frees[c]
        result.append(c)

        for vv in v:
            in_degree[vv] -= 1
            if in_degree[vv] == 0:
                next_courses.append(vv)

    if len(result) == numCourses:
        return result

    return []
