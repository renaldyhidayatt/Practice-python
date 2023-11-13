def myAtoi(s: str) -> int:
    maxInt = (
        2 << 30
    )  # Mendefinisikan nilai maksimum yang dapat ditampung dalam tipe data int

    # Inisialisasi variabel-variabel yang akan digunakan
    signAllowed, whitespaceAllowed, sign, digits = True, True, 1, []

    for c in s:
        # Melewati spasi awal
        if c == " " and whitespaceAllowed:
            continue

        # Menangani tanda positif atau negatif
        if signAllowed:
            if c == "+":
                signAllowed = False
                whitespaceAllowed = False
                continue
            elif c == "-":
                sign = -1
                signAllowed = False
                whitespaceAllowed = False
                continue

        # Memeriksa apakah karakter merupakan digit
        if c < "0" or c > "9":
            break

        whitespaceAllowed = False
        signAllowed = False
        digits.append(
            ord(c) - ord("0")
        )  # Mengubah karakter digit ke nilai angka dan menambahkannya ke list

    # Mengonversi digit ke integer
    num, place = 0, 1

    lastLeadingOfIndex = -1
    for i, d in enumerate(digits):
        if d == 0:
            lastLeadingOfIndex = i
        else:
            break

    # Mengatasi angka dengan leading zeros
    if lastLeadingOfIndex > -1:
        digits = digits[lastLeadingOfIndex + 1 :]

    # Menentukan nilai maksimum yang dapat di-return berdasarkan tanda
    if sign > 0:
        rtnMax = maxInt - 1
    else:
        rtnMax = maxInt

    digitsCount = len(digits)

    # Mengonversi digit ke integer
    for i in range(digitsCount - 1, -1, -1):
        num += digits[i] * place
        place *= 10
        # Memeriksa apakah hasil melebihi batas nilai maksimum yang dapat di-return
        if digitsCount - i > 10 or num > rtnMax:
            return int(sign * rtnMax)

    num *= sign  # Mengalikan dengan tanda

    return int(num)  # Mengembalikan hasil konversi ke tipe data integer
