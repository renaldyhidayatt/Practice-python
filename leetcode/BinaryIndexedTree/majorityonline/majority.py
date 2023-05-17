import bisect
from typing import List, Tuple


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.data = arr
        self.segment_tree = [None] * (4 * len(arr))
        self.count = {}

    def merge(i: Tuple, j: Tuple) -> Tuple:
        if i[0] == j[0]:
            return i[0], i[1] + j[1]
        elif i[1] > j[1]:
            return i[0], i[1] - j[1]
        else:
            return j[0], j[1] - i[1]

    def build_segment_tree(self, tree_index: int, left: int, right: int) -> tuple:
        if left == right:
            self.segment_tree[tree_index] = (self.arr[left], 1)
        else:
            mid_tree_index = left + (right - left) // 2
            left_tree_index = self.left_child(tree_index)
            right_tree_index = self.right_child(tree_index)
            self.build_segment_tree(left_tree_index, left, mid_tree_index)
            self.build_segment_tree(right_tree_index, mid_tree_index + 1, right)
            self.segment_tree[tree_index] = self.merge(
                self.segment_tree[left_tree_index], self.segment_tree[right_tree_index]
            )

        self.build_segment_tree(0, 0, len(self.arr) - 1)

        for i, num in enumerate(self.arr):
            if num not in self.count:
                self.count[num] = []
            self.count[num].append(i)

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2

    def query_in_tree(
        self, tree_index: int, left: int, right: int, query_left: int, query_right: int
    ) -> tuple:
        mid_tree_index = left + (right - left) // 2
        left_tree_index = self.left_child(tree_index)
        right_tree_index = self.right_child(tree_index)

        if query_left <= left and query_right >= right:
            return self.segment_tree[tree_index]
        elif query_left > mid_tree_index:
            return self.query_in_tree(
                right_tree_index, mid_tree_index + 1, right, query_left, query_right
            )
        elif query_right <= mid_tree_index:
            return self.query_in_tree(
                left_tree_index, left, mid_tree_index, query_left, query_right
            )
        else:
            return self.merge(
                self.query_in_tree(
                    left_tree_index, left, mid_tree_index, query_left, mid_tree_index
                ),
                self.query_in_tree(
                    right_tree_index,
                    mid_tree_index + 1,
                    right,
                    mid_tree_index + 1,
                    query_right,
                ),
            )

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate, count = self.query(left, right)

        if candidate not in self.count:
            return -1

        start = bisect.bisect_left(self.count[candidate], left)
        end = bisect.bisect_right(self.count[candidate], right)

        if end - start >= threshold:
            return candidate
        else:
            return -1
