from collections import deque


def canFinish(n, pre):
    in_degree = [0] * n
    frees = [[] for _ in range(n)]
    next_courses = deque()

    for v in pre:
        in_degree[v[0]] += 1
        frees[v[1]].append(v[0])

    for i in range(n):
        if in_degree[i] == 0:
            next_courses.append(i)

    while next_courses:
        c = next_courses.popleft()
        v = frees[c]

        for vv in v:
            in_degree[vv] -= 1
            if in_degree[vv] == 0:
                next_courses.append(vv)

    return sum(in_degree) == 0
