class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode):
    dummy = ListNode(next=head)
    pt = dummy
    while pt is not None and pt.next is not None and pt.next.next is not None:
        pt.next, pt.next.next, pt.next.next.next, pt = (
            pt.next.next,
            pt.next,
            pt.next.next.next,
            pt.next,
        )
    return dummy.next
