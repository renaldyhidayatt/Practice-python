def findTheDiffrence(s: str, t: str):
    n, ch = len(t), ord(t[n - 1])

    for i in range(n - 1):
        ch ^= ord(s[i])
        ch ^= ord(t[i])

    return chr(ch)
