from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode) -> List[int]:
    res: List[int] = []

    if root == None:
        return res

    queue: List[TreeNode] = [root]

    while queue:
        n = len(queue)

        for i in n:
            if queue[i].left != None:
                queue.append(queue[i].left)

            if queue[i].right != None:
                queue.append(queue[i].right)

        res.append(queue[n - 1].val)

        queue = queue[n:]

    return res
