class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    pass


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
        return False
    elif p != None and q == None:
        if p.val != q.val:
            return False
        return isSameTree(p.Left, q.Left) and isSameTree(p.Right, q.Right)
    else:
        return False


def invertTree(root: TreeNode) -> TreeNode:
    if root == None:
        return None

    invertTree(root.Left)
    invertTree(root.Right)

    root.Left, root.Right = root.Right, root.Left

    return root
