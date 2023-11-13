from typing import List


class Interval:
    def __init__(self, s: int = 0, e: int = 0):
        self.start = s
        self.end = e


def insert(intervals: List[Interval], newInterval: Interval) -> List[Interval]:
    res = []
    if not intervals:
        res.append(newInterval)
        return res

    curIndex = 0
    while curIndex < len(intervals) and intervals[curIndex].end < newInterval.start:
        res.append(intervals[curIndex])
        curIndex += 1

    while curIndex < len(intervals) and intervals[curIndex].start <= newInterval.end:
        newInterval.start = min(newInterval.start, intervals[curIndex].start)
        newInterval.end = max(newInterval.end, intervals[curIndex].end)
        curIndex += 1

    res.append(newInterval)

    while curIndex < len(intervals):
        res.append(intervals[curIndex])
        curIndex += 1

    return res
