from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0  # Inisialisasi luas maksimum wadah
    start = 0  # Pointer untuk titik awal dari wadah
    end = len(height) - 1  # Pointer untuk titik akhir dari wadah

    while start < end:
        width = end - start  # Lebar dari wadah
        h = min(
            height[start], height[end]
        )  # Tinggi wadah ditentukan oleh minimum tinggi dari dua titik
        area = width * h  # Luas wadah adalah lebar dikalikan tinggi

        if area > max_area:
            max_area = area  # Memperbarui luas maksimum jika luas yang dihitung saat ini lebih besar

        # Menggeser pointer titik awal atau akhir berdasarkan tinggi dari masing-masing titik
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return max_area  # Mengembalikan luas maksimum wadah berdasarkan titik yang memberikan hasil terbesar
