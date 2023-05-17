class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    if root == None:
        return 0

    if root.left == None:
        return minDepth(root.right) + 1

    if root.right == None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1
