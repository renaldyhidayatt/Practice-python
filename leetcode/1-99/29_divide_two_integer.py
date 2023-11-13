def divide(dividend: int, divisor: int) -> int:
    # Penanganan kasus batas
    if dividend == -2147483648 and divisor == -1:
        return 2147483647

    # Inisialisasi hasil, penentuan tanda
    result = 0
    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1

    # Mengambil nilai absolut dari kedua bilangan
    dvd, dvs = abs(dividend), abs(divisor)

    # Melakukan pembagian menggunakan operasi bit
    while dvd >= dvs:
        temp = dvs
        m = 1

        # Mencari faktor yang dapat dikalikan dengan divisor
        while (temp << 1) <= dvd:
            temp <<= 1
            m <<= 1

        # Mengurangi nilai dividend dengan temp (faktor yang ditemukan)
        dvd -= temp
        result += m  # Menambahkan hasil pembagian

    return sign * result  # Mengembalikan hasil akhir dengan mempertimbangkan tanda
