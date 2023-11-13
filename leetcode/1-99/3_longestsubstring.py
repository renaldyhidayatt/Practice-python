def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0  # Jika string kosong, panjang substring terpanjang adalah 0
    freq = [0] * 128  # Inisialisasi array frekuensi untuk karakter ASCII
    result, left, right = (
        0,
        0,
        -1,
    )  # Inisialisasi variabel hasil, pointer kiri, dan pointer kanan

    while left < len(s):
        if (
            right + 1 < len(s) and freq[ord(s[right + 1])] == 0
        ):  # Jika karakter belum ada dalam substring saat ini
            freq[ord(s[right + 1])] += 1  # Tambahkan karakter ke dalam substring
            right += 1  # Geser pointer kanan ke kanan
        else:
            freq[ord(s[left])] -= 1  # Kurangi frekuensi karakter di kiri dari substring
            left += 1  # Geser pointer kiri ke kanan
        result = max(
            result, right - left + 1
        )  # Perbarui panjang substring terpanjang yang ditemukan
    return result  # Kembalikan panjang dari substring terpanjang yang tidak memiliki karakter berulang


print(lengthOfLongestSubstring("abcabcbb"))
