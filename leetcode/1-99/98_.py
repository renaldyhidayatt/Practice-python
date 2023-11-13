from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def is_valid_bst(root: TreeNode) -> bool:
    return is_valid_bst_recursive(root, float("-inf"), float("inf"))


def is_valid_bst_recursive(root: TreeNode, minimum: float, maximum: float) -> bool:
    if not root:
        return True
    val = root.val
    return (
        minimum < val < maximum
        and is_valid_bst_recursive(root.left, minimum, val)
        and is_valid_bst_recursive(root.right, val, maximum)
    )
