from typing import List


def generateParenthesis(n):
    if n == 0:
        return []  # Mengembalikan list kosong jika n adalah 0

    res = []  # List untuk menampung hasil kombinasi tanda kurung
    findGenerateParenthesis(
        n, n, "", res
    )  # Memanggil fungsi rekursif untuk menemukan kombinasi

    return res  # Mengembalikan hasil kombinasi tanda kurung


def findGenerateParenthesis(lindex: int, rindex: int, string: str, res: List):
    if lindex == 0 and rindex == 0:
        res.append(
            string
        )  # Jika tanda kurung terbuka dan tutup sudah seimbang, tambahkan kombinasi ke dalam hasil
        return

    if lindex > 0:
        findGenerateParenthesis(
            lindex - 1, rindex, string + "(", res
        )  # Tambahkan tanda kurung buka
    if rindex > 0 and lindex < rindex:
        findGenerateParenthesis(
            lindex, rindex - 1, string + ")", res
        )  # Tambahkan tanda kurung tutup jika sesuai
