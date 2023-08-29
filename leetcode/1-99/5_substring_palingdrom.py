def longestPalingrome(s: str):
    if len(s) == 0:
        return ""

    left, right, pl, pr = 0, -1, 0, 0
    while left < len(s):
        while right + 1 < len(s) and s[left] == s[right + 1]:
            right += 1
        while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        if right - left > pr - pl:
            pl, pr = left, right
        left = (left + right) // 2 + 1
        right = left
    return s[pl : pr + 1]
