class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode) -> ListNode:
    if head is None:
        return head

    nil_node = ListNode(0)
    nil_node.next = head

    head = nil_node

    last_val = 0

    while head.next is not None and head.next.next is not None:
        if head.next.val == head.next.next.val:
            last_val = head.next.val

            while head.next is not None and last_val == head.next.val:
                head.next = head.next.next

        else:
            head = head.next

    return nil_node.next
