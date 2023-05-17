def hashAllCodes(s: str, k: int) -> bool:
    need = 2**k

    visited = [False] * need

    mask, curr = (1 << k) - 1, 0

    for i in range(len(s)):
        curr = ((curr << 1) | int(s[i])) & mask

        if i >= k - 1:
            if not visited[curr]:
                need -= 1
                visited[curr] = True

                if need == 0:
                    return True

    return False
