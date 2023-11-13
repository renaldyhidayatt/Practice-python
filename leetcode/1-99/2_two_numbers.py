class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Inisialisasi node kepala yang menampung hasil penjumlahan
    head = ListNode(0)
    n1, n2, carry, current = 0, 0, 0, head

    # Iterasi melalui kedua linked list dan penanganan carry jika diperlukan
    while l1 is not None or l2 is not None or carry != 0:
        # Atur nilai node saat ini atau 0 jika node pada linked list sudah habis
        if l1 is None:
            n1 = 0
        else:
            n1 = l1.val
            l1 = l1.next  # Lanjut ke node berikutnya

        if l2 is None:
            n2 = 0
        else:
            n2 = l2.val
            l2 = l2.next  # Lanjut ke node berikutnya

        # Hitung nilai penjumlahan dan carry, serta buat node berikutnya pada linked list hasil
        current.next = ListNode((n1 + n2 + carry) % 10)
        current = current.next
        carry = (n1 + n2 + carry) // 10

    # Kembalikan linked list hasil dari node setelah kepala
    return head.next  # type: ignore
