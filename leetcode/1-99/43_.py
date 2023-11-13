def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    tmp = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        for j in range(len(num2)):
            tmp[i + j + 1] += int(num1[i]) * int(num2[j])

    for i in range(len(tmp) - 1, 0, -1):
        tmp[i - 1] += tmp[i] // 10
        tmp[i] %= 10

    if tmp[0] == 0:
        tmp = tmp[1:]

    res = [chr(ord("0") + digit) for digit in tmp]
    return "".join(res)
