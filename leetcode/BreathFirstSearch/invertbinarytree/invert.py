class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    invertTree(root.left)
    invertTree(root.right)

    root.left, root.right = root.right, root.left
    return root
