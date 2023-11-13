from collections import defaultdict


def minWindow(s, t):
    if not s or not t:
        return ""

    t_freq, s_freq = defaultdict(int), defaultdict(int)
    result, left, right, final_left, final_right, min_w, count = (
        "",
        0,
        -1,
        -1,
        -1,
        len(s) + 1,
        0,
    )

    for i in range(len(t)):
        t_freq[t[i]] += 1

    while left < len(s):
        if right + 1 < len(s) and count < len(t):
            s_freq[s[right + 1]] += 1
            if s_freq[s[right + 1]] <= t_freq[s[right + 1]]:
                count += 1
            right += 1
        else:
            if right - left + 1 < min_w and count == len(t):
                min_w = right - left + 1
                final_left = left
                final_right = right
            if s_freq[s[left]] == t_freq[s[left]]:
                count -= 1
            s_freq[s[left]] -= 1
            left += 1

    if final_left != -1:
        result = s[final_left : final_right + 1]

    return result
