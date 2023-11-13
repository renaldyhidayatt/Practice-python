def isPalindrome(x: int) -> bool:
    if x < 0:
        return False  # Jika angka negatif, bukan palindrome
    if x == 0:
        return True  # Jika angka nol, dianggap palindrome

    if x % 10 == 0:
        return False  # Jika angka berakhiran 0, tidak mungkin palindrome (kecuali nol itu sendiri)

    arr = []

    # Membuat array dari digit-digit angka untuk memeriksa apakah bersifat palindrome
    while x > 0:
        arr.append(x % 10)
        x = x // 10

    sz = len(arr)
    for i in range(sz // 2):
        if arr[i] != arr[sz - i - 1]:
            return False  # Membandingkan digit pertama dengan yang terakhir, kedua dengan yang sebelum terakhir, dan seterusnya

    return True  # Jika tidak ada perbedaan antara digit pertama dan terakhir, kedua dan sebelum terakhir, dan seterusnya, maka angka adalah palindrome


print(isPalindrome(121))
