def combine(n, k):
    if n <= 0 or k <= 0 or k > n:
        return []

    res = []
    c = []

    def generate_combinations(start, c):
        if len(c) == k:
            res.append(c[:])
            return

        for i in range(start, n - (k - len(c)) + 2):
            c.append(i)
            generate_combinations(i + 1, c)
            c.pop()

    generate_combinations(1, c)
    return res
