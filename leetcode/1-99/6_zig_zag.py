def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s  # Jika numRows adalah 1 atau lebih besar atau sama dengan panjang s, langsung kembalikan s

    # Membuat matriks kosong dengan jumlah baris sesuai numRows
    matrix = [[] for _ in range(numRows)]
    down, up = 0, numRows - 2  # Pointer untuk pergerakan diagonal ke bawah dan ke atas

    for i in range(len(s)):
        if down != numRows:
            matrix[down].append(s[i])  # Tambahkan karakter ke baris ke bawah

            down += 1  # Geser ke baris berikutnya

        elif up > 0:
            matrix[up].append(s[i])  # Tambahkan karakter ke baris diagonal ke atas
            up -= 1  # Geser ke atas untuk membuat pola zig-zag

        else:
            up = numRows - 2  # Reset pointer untuk pola diagonal ke atas
            down = 0  # Reset pointer untuk pola diagonal ke bawah

    solution = ""

    # Gabungkan karakter dari matriks menjadi satu string hasil
    for row in matrix:
        solution += "".join(row)

    return solution  # Kembalikan hasil konversi string dengan pola zig-zag berdasarkan numRows


print(convert("PAYPALISHIRING", 4))
