from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]):
    length = len(lists)

    if length < 1:
        return None  # Jika tidak ada list, mengembalikan None

    if length == 1:
        return lists[0]  # Jika hanya satu list, mengembalikan list tersebut

    num = length // 2  # Membagi daftar menjadi dua bagian
    left = mergeKLists(lists[:num])  # Rekursi pada setengah pertama daftar
    right = mergeKLists(lists[num:])  # Rekursi pada setengah kedua daftar
    return mergeTwoList(
        left, right
    )  # Menggabungkan kedua bagian dengan fungsi mergeTwoList


def mergeTwoList(l1: ListNode, l2: ListNode):
    if l1 is None:
        return l2  # Jika salah satu list kosong, mengembalikan list lainnya

    if l2 is None:
        return l1  # Jika salah satu list kosong, mengembalikan list lainnya

    if l1.val < l2.val:
        l1.next = mergeTwoList(
            l1.next, l2
        )  # Menyusun kembali list dengan nilai terkecil di depan
        return l1

    l2.next = mergeTwoList(
        l1, l2.next
    )  # Menyusun kembali list dengan nilai terkecil di depan
    return l2
