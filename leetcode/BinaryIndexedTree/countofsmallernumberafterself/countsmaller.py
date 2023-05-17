from typing import List


class BinarySearchTreeNode:
    def __init__(self, value) -> None:
        self.val = value

        self.less = 0
        self.count = 1
        self.left = None
        self.right = None

    def insert(self, value, numLessThan):
        if value < self.val:
            self.less += 1

            if not self.left:
                self.left = BinarySearchTreeNode(value)
            else:
                self.left.insert(value, numLessThan)

        elif value > self.val:
            numLessThan[0] += self.less + self.count

            if not self.right:
                self.right = BinarySearchTreeNode(value)
            else:
                self.right.insert(value, numLessThan)

        else:
            numLessThan[0] += self.less
            self.count += 1


class BinarySearchTree:
    def __init__(self, value) -> None:
        self.root = BinarySearchTreeNode(value)

    def freeTree(self, root: BinarySearchTreeNode):
        if not root:
            return

        if root.left:
            self.freeTree(root.left)

        if root.right:
            self.freeTree(root.right)

        root = None

    def insert(self, value, numLessThan):
        self.root.insert(value, numLessThan)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)

        if len(nums) == 0:
            return counts

        tree = BinarySearchTree(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            numLessThan = [0]

            tree.insert(nums[i], numLessThan)

            counts[i] = numLessThan[0]

            tree.freeTree(tree.root)

            return counts


s = Solution()
nums = [5, 2, 6, 1]

counts = s.countSmaller(nums)

print(counts)
