def longestPalindrome(s: str):
    if len(s) == 0:
        return ""  # Jika string kosong, maka tidak ada palindrome, kembalikan string kosong

    left, right, pl, pr = 0, -1, 0, 0  # Inisialisasi pointer kiri, kanan, dan indeks palindrome terpanjang

    while left < len(s):
        # Mencari karakter yang sama ke kanan (bisa lebih dari satu karakter)
        while right + 1 < len(s) and s[left] == s[right + 1]:
            right += 1

        # Ekspansi untuk mencari palindrome
        while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1

        # Memeriksa dan memperbarui indeks palindrome terpanjang yang ditemukan
        if right - left > pr - pl:
            pl, pr = left, right

        # Geser pointer ke tengah string
        left = (left + right) // 2 + 1
        right = left

    return s[pl: pr + 1]  # Kembalikan substring dari indeks palindrome terpanjang yang ditemukan
