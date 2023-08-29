def myAtoi(s: str) -> int:
    maxInt = 2 << 30
    signAllowed, whitespaceAllowed, sign, digits = True, True, 1, []

    for c in s:
        if c == " " and whitespaceAllowed:
            continue

        if signAllowed:
            if c == "+":
                signAllowed = False
                whitespaceAllowed = False
                continue

            elif c == "-":
                sign = -1
                signAllowed = False
                whitespaceAllowed = False
                continue

        if c < "0" or c > "9":
            break

        whitespaceAllowed = False
        signAllowed = False
        digits.append(ord(c) - ord("0"))

    num, place = 0, 1

    lastLeadingOfIndex = -1
    for i, d in enumerate(digits):
        if d == 0:
            lastLeadingOfIndex = i
        else:
            break

    if lastLeadingOfIndex > -1:
        digits = digits[lastLeadingOfIndex + 1 :]

    if sign > 0:
        rtnMax = maxInt - 1
    else:
        rtnMax = maxInt

    digitsCount = len(digits)

    for i in range(digitsCount - 1, -1, -1):
        num += digits[i] * place
        place *= 10
        if digitsCount - i > 10 or num > rtnMax:
            return int(sign * rtnMax)

    num *= sign

    return int(num)
