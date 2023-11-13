
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def deleteDupliates(head: ListNode) -> ListNode:
    cur = head

    if head in None:
        return None
    
    if head.next is None:
        return head
    
    while cur.next is not None:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    
    return head
