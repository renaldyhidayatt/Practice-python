from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # Mengambil string pertama sebagai acuan untuk prefix umum
    prefix = strs[0]

    # Iterasi melalui setiap string pada list
    for i in range(1, len(strs)):
        j = 0
        # Membandingkan setiap karakter di prefix dengan karakter pada string saat ini
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1

        # Memperbarui prefix untuk hanya menyertakan karakter yang cocok sampai saat ini
        prefix = prefix[:j]

    return prefix  # Mengembalikan prefix umum terpanjang yang ditemukan di semua string
