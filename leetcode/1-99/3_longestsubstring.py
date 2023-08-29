def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    freq = [0] * 128
    result, left, right = 0, 0, -1

    while left < len(s):
        if right + 1 < len(s) and freq[ord(s[right + 1])] == 0:
            freq[ord(s[right + 1])] += 1
            right += 1
        else:
            freq[ord(s[left])] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


print(lengthOfLongestSubstring("abcabcbb"))
