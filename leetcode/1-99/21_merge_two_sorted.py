class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoList(l1: ListNode, l2: ListNode):
    if l1 is None:
        return l2  # Jika salah satu linked list kosong, mengembalikan linked list yang lainnya

    if l2 is None:
        return l1  # Jika salah satu linked list kosong, mengembalikan linked list yang lainnya

    if l1.val < l2.val:
        l1.next = mergeTwoList(
            l1.next, l2
        )  # Jika nilai pertama lebih kecil, rekursi untuk list selanjutnya
        return l1

    l2.next = mergeTwoList(
        l1, l2.next
    )  # Jika nilai kedua lebih kecil, rekursi untuk list selanjutnya
    return l2
