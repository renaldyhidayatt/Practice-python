class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, sum: int) -> bool:
    if root == None:
        return False

    if root.Left == None and root.Right == None:
        return sum == root.Val

    return hasPathSum(root.Left, sum - root.Val) or hasPathSum(
        root.Right, sum - root.Val
    )
