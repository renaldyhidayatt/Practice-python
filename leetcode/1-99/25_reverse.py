class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    node = head
    for i in range(k):
        if node is None:
            return head

        node = node.next

    new_head = reverse(head, node) # type: ignore
    head.next = reverseKGroup(node, k) # type: ignore
    return new_head


def reverse(first: ListNode, last: ListNode) -> ListNode:
    prev = last
    while first != last:
        tmp = first.next
        first.next = prev
        prev = first
        first = tmp # type: ignore

    return prev
