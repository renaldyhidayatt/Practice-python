class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
        return True
    elif p != None and q == None:
        if p.val != q.val:
            return False

        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
