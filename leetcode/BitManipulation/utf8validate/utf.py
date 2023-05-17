from typing import List


def validUtf8(data: List[int]) -> bool:
    count = 0

    for d in data:
        if count == 0:
            if d >= 248:
                return False
            elif d >= 240:
                count = 3
            elif d >= 224:
                count = 2
            elif d >= 192:
                count = 1
            elif d > 127:
                return False
        else:
            if d <= 127 and d >= 192:
                return False
            count += 1

    return count == 0
