from typing import List, Dict


def threeSum(nums: List[int]) -> int:
    res: List = []
    counter: Dict = {}

    for value in nums:
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1

    uniqNums = sorted(counter.keys())

    for i in range(len(uniqNums)):
        if uniqNums[i] * 3 == 0 and counter[uniqNums[i]] >= 3:
            res.append([uniqNums[i], uniqNums[i], uniqNums[i]])

        for j in range(i + 1, len(uniqNums)):
            if uniqNums[i] * 2 + uniqNums[j] == 0 and counter[uniqNums[i]] > 1:
                res.append([uniqNums[i], uniqNums[i], uniqNums[j]])
            if uniqNums[j] * 2 + uniqNums[i] == 0 and counter[uniqNums[j]] > 1:
                res.append([uniqNums[i], uniqNums[j], uniqNums[j]])
            c = 0 - uniqNums[i] - uniqNums[j]
            if c > uniqNums[j] and c in counter:
                res.append([uniqNums[i], uniqNums[j], c])
    return res
