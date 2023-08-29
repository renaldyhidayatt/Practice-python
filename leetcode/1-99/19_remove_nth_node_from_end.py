class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummyHead = ListNode(0)
    dummyHead.next = head
    preSlow, slow, fast = dummyHead, head, head

    while fast is not None:
        if n <= 0:
            preSlow = slow
            slow = slow.next

        n -= 1
        fast = fast.next

    preSlow.next = slow.next

    return dummyHead.next
