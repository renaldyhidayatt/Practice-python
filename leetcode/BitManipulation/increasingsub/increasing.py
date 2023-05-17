from typing import List, Dict


def findSubSequences(nums: List[int]) -> List[List[int]]:
    c, visited, res = [], {}, []

    for i in range(len(nums) - 1):
        if nums[i] in visited:
            continue
        else:
            visited[nums[i]] = True
            generateIncSubSets(nums, i, c, res)

    return res


def generateIncSubSets(
    nums: List[int], current: int, c: List[int], res: List[List[int]]
):
    c.append(nums[current])

    if len(c) >= 2:
        res.append(c[:])

    visited: Dict = []

    for i in range(current + 1, len(nums)):
        if nums[current] <= nums[i]:
            if nums[i] in visited:
                continue
            else:
                visited[nums[i]] = True
                generateIncSubSets(nums=nums, i=i, c=c, res=res)

    c.pop()
