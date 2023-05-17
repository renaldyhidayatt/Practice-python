from typing import List

LEFTSIDE = 1
RIGHTSIDE = 2


class Point:
    def __init__(self, x, side, index) -> None:
        self.xAxis = x
        self.side = side
        self.index = index


def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    res = []
    if len(buildings) == 0:
        return res

    allPoints, bit = [], BinaryIndexedTree()

    for i, b in enumerate(buildings):
        allPoints.append(Point(b[0], LEFTSIDE, i))
        allPoints.append(Point(b[1], RIGHTSIDE, i))
        allPoints.sort(key=lambda p: (p.xAxis, p.side))

    bit.Init(len(allPoints))

    kth = {allPoints[i]: i for i in range(len(allPoints))}

    for i in range(len(allPoints)):
        pt = allPoints[i]
        if pt.side == LEFTSIDE:
            bit.Add(
                kth[Point(buildings[pt.index][1], RIGHTSIDE, pt.index)],
                buildings[pt.index][2],
            )
            currHeight = bit.Query(kth[pt] + 1)
            if len(res) == 0 or res[-1][1] != currHeight:
                if len(res) > 0 and res[-1][0] == pt.xAxis:
                    res[-1][1] = currHeight
                else:
                    res.append([pt.xAxis, currHeight])
    return res


class BinaryIndexedTree:
    def __init__(self):
        self.tree = []
        self.capacity = 0

    def Init(self, capacity):
        self.tree, self.capacity = [0] * (capacity + 1), capacity

    def Add(self, index, val):
        while index > 0:
            self.tree[index] = max(self.tree[index], val)
            index -= index & -index

    def Query(self, index):
        sum = 0
        while index <= self.capacity:
            sum = max(sum, self.tree[index])
            index += index & -index
        return sum
