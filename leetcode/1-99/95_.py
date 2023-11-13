from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: None = None, right: None = None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(n: int) -> List[TreeNode]:
    if n == 0:
        return []
    return generate_bst_tree(1, n)


def generate_bst_tree(start: int, end: int) -> List[TreeNode]:
    tree = []

    if start > end:
        tree.append(None)

        return tree

    for i in range(start, end + 1):
        left = generate_bst_tree(start, i - 1)
        right = generate_bst_tree(i + 1, end)
        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                tree.append(root)
    return tree
