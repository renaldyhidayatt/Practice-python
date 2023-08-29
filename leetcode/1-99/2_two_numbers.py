class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    n1, n2, carry, current = 0, 0, 0, head
    while l1 is not None or l2 is not None or carry != 0:
        if l1 is None:
            n1 = 0
        else:
            n1 = l1.val
            l1 = l1.next # type: ignore
        if l2 is None:
            n2 = 0
        else:
            n2 = l2.val
            l2 = l2.next # type: ignore
        current.next = ListNode((n1 + n2 + carry) % 10)
        current = current.next
        carry = (n1 + n2 + carry) // 10
    return head.next # type: ignore
