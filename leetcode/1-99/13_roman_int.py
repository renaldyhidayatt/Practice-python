roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    if s == "":
        return 0  # Jika string kosong, mengembalikan nilai 0

    num, lastInt, total = 0, 0, 0

    for i in range(len(s)):
        # Mengambil karakter dari belakang satu per satu untuk memproses bilangan Romawi
        char = s[len(s) - (i + 1) : len(s) - i]
        num = roman[char]  # Mengonversi karakter Romawi ke nilai angka

        if num < lastInt:
            total = (
                total - num
            )  # Jika nilai saat ini lebih kecil dari nilai sebelumnya, kurangi dari total
        else:
            total = (
                total + num
            )  # Jika nilai saat ini tidak lebih kecil dari nilai sebelumnya, tambahkan ke total

        lastInt = num  # Memperbarui nilai sebelumnya untuk perbandingan selanjutnya

    return total  # Mengembalikan total sebagai hasil konversi dari bilangan Romawi ke angka


# Contoh pemanggilan fungsi
print(romanToInt("LVIII"))
