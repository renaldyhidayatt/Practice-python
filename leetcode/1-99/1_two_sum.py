from typing import List

def twoSum(nums: List, target: int) -> List[int]:
    m = {}

    for i in range(len(nums)):
        another = target - nums[i]

        if another in m:
            return [m[another], i]
        
        m[nums[i]] = i

    return None # type: ignore
