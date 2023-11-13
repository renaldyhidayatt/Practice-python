class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    node = head
    for i in range(k):
        if node is None:
            return head  # Jika jumlah node tidak mencapai k, kembalikan keadaan awal

        node = node.next

    new_head = reverse(head, node)  # Balikkan setiap k node dalam linked list
    head.next = reverseKGroup(
        node, k
    )  # Rekursi untuk bagian berikutnya dari linked list
    return new_head  # Mengembalikan linked list yang telah dibalikkan k node


def reverse(first: ListNode, last: ListNode) -> ListNode:
    prev = last
    while first != last:
        tmp = first.next
        first.next = prev
        prev = first
        first = tmp  # Lanjut ke node selanjutnya

    return (
        prev  # Mengembalikan head dari setiap bagian linked list yang telah dibalikkan
    )
