class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    if not intervals:
        return intervals

    def takeFirst(elem):
        return elem.start

    intervals.sort(key=takeFirst)
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i].start > res[-1].end:
            res.append(intervals[i])
        else:
            res[-1].end = max(res[-1].end, intervals[i].end)
    return res
