from typing import List


def twoSum(nums: List, target: int) -> List[int]:
    m = {}  # Inisialisasi dictionary untuk menyimpan nilai yang sudah dilihat

    for i in range(len(nums)):  # Iterasi melalui list nums
        another = (
            target - nums[i]
        )  # Hitung nilai lain yang dibutuhkan untuk mencapai target dari nilai saat ini

        if another in m:  # Jika nilai lain sudah ada dalam dictionary
            return [
                m[another],
                i,
            ]  # Kembalikan indeks dari nilai lain dan nilai saat ini

        m[nums[i]] = i  # Simpan nilai dan indeksnya dalam dictionary

    return None  # Jika tidak ditemukan pasangan yang sesuai, kembalikan None
