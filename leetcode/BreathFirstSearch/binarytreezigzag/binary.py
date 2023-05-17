from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    search(root, 0, res)
    return res


def search(root: TreeNode, depth: int, res: List[List[int]]) -> None:
    if not root:
        return
    if len(res) < depth + 1:
        res.append([])
    if depth % 2 == 0:
        res[depth].append(root.val)
    else:
        res[depth].insert(0, root.val)
    search(root.left, depth + 1, res)
    search(root.right, depth + 1, res)
