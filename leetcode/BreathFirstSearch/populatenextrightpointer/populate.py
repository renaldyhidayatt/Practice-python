from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Node) -> Node:
    if root == None:
        return root

    q: Node = [root]

    while len(q) > 0:
        p: List[Node] = []

        for i, node in enumerate(q):
            if i + 1 < len(q):
                node.next = q[i + 1]

            if node.left:
                p.append(node.left)

            if node.right:
                p.append(node.right)

        q = p

    return root
