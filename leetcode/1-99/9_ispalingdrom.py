def isPalingdrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True

    if x % 10 == 0:
        return False

    arr = []

    while x > 0:
        arr.append(x % 10)
        x = x // 10

    sz = len(arr)
    for i in range(sz // 2):
        if arr[i] != arr[sz - i - 1]:
            return False

    return True


print(isPalingdrome(121))
