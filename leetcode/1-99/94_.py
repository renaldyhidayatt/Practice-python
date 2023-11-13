from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    result = []
    inorder(root, result)

    return result


def inorder(root: TreeNode, output: List[int]):
    if root:
        inorder(root.left, output=output)
        output.append(root.val)
        inorder(root.right, output)
