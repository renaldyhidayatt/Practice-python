from typing import List


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        sz = len(nums)
        numsArr = [0] * (sz + 1)
        sumsArr = [0] * (sz + 1)
        self.sz = sz
        self.nums = numsArr
        self.sums = sumsArr
        for i in range(sz):
            self.update(i, nums[i])

    def update(self, i: int, val: int) -> None:
        oldv = self.nums[i + 1]
        for idx in range(i + 1, self.sz + 1, idx & -idx):
            self.sums[idx] = self.sums[idx] - oldv + val
        self.nums[i + 1] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.sumRangee(j + 1) - self.sumRangee(i)

    def sumRangee(self, i: int) -> int:
        ret = 0
        for idx in range(i, 0, -(idx & -idx)):
            ret += self.sums[idx]
        return ret
