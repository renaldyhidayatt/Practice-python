def isValid(s: str) -> bool:
    if len(s) == 0:  # Jika string kosong, dianggap valid secara default
        return True

    stack = []  # Stack untuk menyimpan tanda kurung, kurawal, dan siku yang terbuka

    for v in s:  # Iterasi setiap karakter dalam string
        if v in ["[", "(", "{"]:  # Jika karakter adalah tanda buka
            stack.append(v)  # Masukkan ke dalam stack

        # Jika karakter adalah tanda tutup dan sesuai dengan tanda terakhir yang masih terbuka
        elif (
            (v == "]" and stack and stack[-1] == "[")
            or (v == ")" and stack and stack[-1] == "(")
            or (v == "}" and stack and stack[-1] == "{")
        ):
            stack.pop()  # Hapus tanda terbuka yang sesuai dari stack

        else:  # Jika tanda tutup tidak sesuai dengan tanda terbuka terakhir pada stack
            return False  # Tanda kurung tidak seimbang, mengembalikan False

    return (
        len(stack) == 0
    )  # Mengembalikan True jika semua tanda terbuka tertutup secara benar, jika tidak, mengembalikan False
