def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] != 10:
            return digits

        digits[i] = 0

    # all carry
    digits[0] = 1
    digits.append(0)
    return digits
