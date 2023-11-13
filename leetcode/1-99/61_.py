class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    new_head = ListNode(0)

    new_head.next = head
    length = 0

    cur = new_head

    while cur.next:
        length += 1
        cur = cur.next

    if k % length == 0:
        return head

    cur.next = head
    cur = new_head

    for i in range(length - k % length):
        cur = cur.next

    res = ListNode[0]

    res.next = cur.next
    cur.next = None

    return res.Next
