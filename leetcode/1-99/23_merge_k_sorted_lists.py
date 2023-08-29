from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]):
    length = len(lists)

    if length < 1:
        return None

    if length == 1:
        return lists[0]

    num = length // 2
    left = mergeKLists(lists[:num])
    right = mergeKLists(lists[num:])
    return mergeTwoList(left, right)


def mergeTwoList(l1: ListNode, l2: ListNode):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoList(l1.next, l2) # type: ignore
        return l1
    l2.next = mergeTwoList(l1, l2.next) # type: ignore
    return l2
