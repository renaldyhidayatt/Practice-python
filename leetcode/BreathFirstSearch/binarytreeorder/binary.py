from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    queue = [root]
    res = []

    while queue:
        level_size = len(queue)

        tmp = []

        for i in range(level_size):
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)

            tmp.append(queue[i].val)

        queue = queue[level_size:]
        res.append(tmp)

    return res
