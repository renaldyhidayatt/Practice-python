def findSubstring(s, words):
    if len(words) == 0:
        return []
    res = []
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1
    length = len(words[0])
    totalLen = length * len(words)
    tmpCounter = counter.copy()
    for i in range(len(s) - length + 1):
        start = i
        while start < len(s) - length + 1:
            if tmpCounter.get(s[start : start + length], 0) > 0:
                tmpCounter[s[start : start + length]] -= 1
                if checkWords(tmpCounter) and (i + length - start == totalLen):
                    res.append(i)
                start += length
            else:
                break
        tmpCounter = counter.copy()
    return res


def checkWords(s):
    for v in s.values():
        if v > 0:
            return False
    return True
