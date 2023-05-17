

def reverseBits(num):
    res = 0;

    for i in range(32):
        res = res << 1 | num & 1
        num >>= 1
    return res
