def reverse(x: int) -> int:
    tmp = 0  # Variabel sementara untuk menyimpan hasil pembalikan angka
    sign = (
        1 if x >= 0 else -1
    )  # Menyimpan tanda dari angka, 1 untuk positif, -1 untuk negatif

    x = abs(
        x
    )  # Mengubah angka menjadi positif untuk diproses pembalikan digit per digit

    while x != 0:
        tmp = tmp * 10 + x % 10  # Memproses pembalikan angka satu digit demi satu
        x = x // 10  # Mengurangi digit yang sudah diproses

    if tmp > (1 << 31) - 1 or tmp < -(1 << 31):
        return 0  # Memeriksa apakah hasil pembalikan melebihi batas 32-bit, jika ya, kembalikan 0

    return (
        tmp * sign
    )  # Kembalikan hasil pembalikan angka dengan mempertimbangkan tanda asli


print(reverse(123))
