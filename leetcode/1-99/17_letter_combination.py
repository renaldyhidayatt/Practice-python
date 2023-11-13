from typing import List

# Pemetaan angka ke huruf sesuai pada keypad telepon
letter_map = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def letterCombinations(digits: str) -> List[int]:
    res = []  # Menampung hasil akhir dari kombinasi huruf

    # Fungsi rekursif untuk menemukan kombinasi huruf dari digit tertentu
    def findCombination(digits: str, index: int, s: str):
        if index == len(digits):  # Jika telah mencapai panjang digit
            res.append(s)  # Tambahkan kombinasi huruf ke dalam hasil
            return

        num = digits[index]
        letters = letter_map[int(num)]  # Ambil daftar huruf sesuai dengan angka digit

        for letter in letters:
            findCombination(
                digits, index + 1, s + letter
            )  # Rekursi untuk menggabungkan huruf ke dalam kombinasi

    if digits:  # Pastikan digit tidak kosong
        findCombination(
            digits, 0, ""
        )  # Panggil fungsi rekursif untuk menemukan kombinasi huruf

    return (
        res  # Mengembalikan semua kombinasi huruf yang memungkinkan sesuai dengan digit
    )
