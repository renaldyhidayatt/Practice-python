def findSubstring(s, words):
    if len(words) == 0:
        return []

    res = []
    counter = {}

    # Menghitung jumlah kata dalam list
    for w in words:
        counter[w] = counter.get(w, 0) + 1

    length = len(words[0])
    totalLen = length * len(words)
    tmpCounter = counter.copy()

    # Melakukan iterasi pada string untuk mencari substrings yang cocok
    for i in range(len(s) - length + 1):
        start = i
        while start < len(s) - length + 1:
            if tmpCounter.get(s[start : start + length], 0) > 0:
                # Mengurangi kemungkinan kata yang ditemukan
                tmpCounter[s[start : start + length]] -= 1
                # Memeriksa apakah semua kata ditemukan dan panjang total sama
                if checkWords(tmpCounter) and (i + length - start == totalLen):
                    res.append(i)
                start += length
            else:
                break

        tmpCounter = counter.copy()

    return res


def checkWords(s):
    # Memeriksa apakah semua kata ditemukan
    for v in s.values():
        if v > 0:
            return False
    return True
