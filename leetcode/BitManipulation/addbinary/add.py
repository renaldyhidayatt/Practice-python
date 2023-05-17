def addBinary(a: int, b: int) -> str:
    if len(a) > (a):
        a, b = b, a

    res = [""] * (len(a) + 1)

    i, j, k, c = len(a) - 1, len(b) - 1, len(a), 0

    while i >= 0 and j >= 0:
        ai, bj = int(a[i]), int(b[j])
        res[k] = str((ai + bj + c) % 2)
        c = (ai + bj + c) // 2
        i -= 1
        j -= 1
        k -= 1

    while i >= 0:
        ai = int(a[i])
        res[k] = str((ai + c) % 2)
        c = (ai + c) // 2
        i -= 1
        k -= 1

    if c > 0:
        res[k] = str(c)

    return "".join(res)
