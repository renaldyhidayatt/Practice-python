class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummyHead = ListNode(
        0
    )  # Membuat simpul kepala palsu untuk menangani kasus di mana simpul pertama dihapus
    dummyHead.next = head  # Menyimpan kepala asli setelah simpul kepala palsu
    preSlow, slow, fast = (
        dummyHead,
        head,
        head,
    )  # Pointer untuk menyimpan posisi saat menjelajah linked list

    while fast is not None:  # Iterasi sampai pointer fast mencapai akhir linked list
        if n <= 0:  # Saat jarak antara slow dan fast sudah sesuai dengan n
            preSlow = (
                slow  # Memindahkan preSlow ke posisi sebelum simpul yang akan dihapus
            )
            slow = slow.next  # Memindahkan slow ke simpul selanjutnya

        n -= 1  # Mengurangi jarak antara slow dan fast
        fast = fast.next  # Memindahkan fast ke simpul berikutnya

    preSlow.next = (
        slow.next
    )  # Menghapus simpul slow dengan mengubah referensi dari preSlow

    return (
        dummyHead.next
    )  # Mengembalikan simpul pertama dari linked list yang telah dimodifikasi
