from typing import Tuple, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def recover_tree(root: TreeNode) -> None:
    prev: Optional[TreeNode] = None
    target1: Optional[TreeNode] = None
    target2: Optional[TreeNode] = None
    _, target1, target2 = in_order_traverse(root, prev, target1, target2)
    if target1 and target2:
        target1.val, target2.val = target2.val, target1.val


def in_order_traverse(
    root: TreeNode,
    prev: Optional[TreeNode],
    target1: Optional[TreeNode],
    target2: Optional[TreeNode],
) -> Tuple[Optional[TreeNode], Optional[TreeNode], Optional[TreeNode]]:
    if not root:
        return prev, target1, target2

    prev, target1, target2 = in_order_traverse(root.left, prev, target1, target2)

    if prev and prev.val > root.val:
        if not target1:
            target1 = prev
        target2 = root

    prev = root
    prev, target1, target2 = in_order_traverse(root.right, prev, target1, target2)

    return prev, target1, target2
