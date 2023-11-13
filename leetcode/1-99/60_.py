def getPermutation(n: int, k: int) -> str:
    if k == 0:
        return ""

    used, p, res = [False] * n, [], [""]
    findPermutation(n, 0, [k], p, res, used)
    return res[0]


def findPermutation(n, index, k, p, res, used):
    if index == n:
        k[0] -= 1

        if k[0] == 0:
            res[0] = "".join(str(v + 1) for v in p)

        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            p.append(i)

            findPermutation(n, index + 1, k, p, res, used)
            p.pop()
            used[i] = False
    return
