def longestValidParentheses(s):
    # Gunakan tumpukan untuk melacak indeks terakhir dari karakter yang cocok
    # Dimulai dengan -1 sebagai indeks awal untuk menghitung panjang awal
    stack = [-1]

    res = 0  # Inisialisasi panjang maksimum urutan tanda kurung

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)  # Tambahkan indeks bukaan tanda kurung ke dalam tumpukan
        else:
            stack.pop()  # Kurangi tumpukan karena tanda kurung tutup ditemukan

            if len(stack) == 0:
                stack.append(
                    i
                )  # Jika tumpukan kosong, gunakan indeks saat ini sebagai referensi baru
            else:
                # Hitung panjang urutan tanda kurung yang valid saat ini dan perbarui res jika diperlukan
                res = max(res, i - stack[-1])

    return res  # Kembalikan panjang urutan tanda kurung terpanjang yang valid
