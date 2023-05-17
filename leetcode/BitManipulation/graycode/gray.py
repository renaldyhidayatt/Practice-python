def grayCode1(n):
    l = 1 << n
    out = [0] * l
    for i in range(l):
        out[i] = (i >> 1) ^ i
        return out
