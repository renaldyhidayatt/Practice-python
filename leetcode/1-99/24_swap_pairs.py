class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode):
    # Membuat node dummy untuk mempermudah penanganan awal linked list
    dummy = ListNode(next=head)
    pt = dummy

    # Melakukan penukaran pasangan node
    while pt is not None and pt.next is not None and pt.next.next is not None:
        # Melakukan penukaran node dengan memanfaatkan assignment tuples
        pt.next, pt.next.next, pt.next.next.next, pt = (
            pt.next.next,  # Node berikutnya setelah pasangan
            pt.next,  # Node pertama dalam pasangan
            pt.next.next.next,  # Node setelah pasangan
            pt.next,  # Node terakhir sebelum penukaran
        )

    return (
        dummy.next
    )  # Mengembalikan linked list setelah dummy yang menunjuk pada linked list awal
