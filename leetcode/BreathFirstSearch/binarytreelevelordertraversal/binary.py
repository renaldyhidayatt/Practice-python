from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    tmp = levelOrder(root)
    res = []

    for i in range(len(tmp) - 1, -1, -1):
        res.append(tmp[i])

    return res


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        levelSize = len(queue)
        levelValues = []
        for i in range(levelSize):
            node = queue.pop(0)
            levelValues.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(levelValues)
    return result
