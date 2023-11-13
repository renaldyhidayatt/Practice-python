def intToRoman(num: int) -> str:
    # Daftar nilai numerik Romawi dan simbol yang sesuai
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""  # String hasil konversi akan disimpan di sini
    i = 0

    # Melakukan konversi dari angka ke bilangan Romawi
    while num != 0:
        while values[i] > num:
            i += 1  # Mencari nilai yang sesuai untuk dikonversi

        num -= values[i]  # Mengurangi nilai yang sudah terkonversi
        res += symbols[i]  # Menambahkan simbol yang sesuai ke hasil konversi

    return res  # Mengembalikan hasil konversi ke bilangan Romawi


# Contoh pemanggilan fungsi
print(intToRoman(3549))
