class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, m, n):
    if not head or m >= n:
        return head

    new_head = ListNode(0)
    new_head.next = head
    pre = new_head

    for count in range(m - 1):
        pre = pre.next

    if not pre.next:
        return head

    cur = pre.next
    for i in range(n - m):
        tmp = pre.nexte
        pre.next = cur.next
        cur.next = cur.next.next
        pre.next.next = tmp

    return new_head.next
 