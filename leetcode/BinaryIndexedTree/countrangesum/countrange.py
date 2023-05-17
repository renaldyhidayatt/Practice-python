class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, val: int) -> None:
        self.insert_node(self.root, val)

    def insert_node(self, root: Node, val: int) -> None:
        if root is None:
            self.root = Node(val)

            return

        root.cnt += 1

        if val < root.val:
            if root.left is None:
                root.left = Node(val)

            else:
                self.insert_node(root.left, val)
        elif val > root.val:
            if root.right is None:
                root.right = Node(val)
            else:
                self.insert_node(root.right, val)

    def less_than(self, sm, val):
        return self.less_than_node(self.root, sm, val, 0)

    def less_than_node(self, root, sm, val, res):
        if root is None:
            return res

        if sm - root.val < val:
            res += root.cnt - self.get_count(root.left)
            return self.less_than_node(root.left, sm, val, res)
        elif sm - root.val > val:
            return self.less_than_node(root.right, sm, val, res)
        else:
            return res + self.get_count(root.right)

    def get_count(self, root):
        if root is None:
            return 0
        return root.cnt


def count_range_sum(nums, lower, upper):
    tree = Tree()

    tree.insert(0)

    s, res = 0, 0

    for n in nums:
        s += n
        lcnt = tree.less_than(s, lower)
        hcnt = tree.less_than(s, upper + 1)
        res += hcnt - lcnt
        tree.insert(s)

    return res
