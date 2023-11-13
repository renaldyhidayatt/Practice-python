import math
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    n = len(nums)
    res = 0  # Variabel untuk menyimpan hasil terdekat dari penjumlahan tiga angka
    diff = math.inf  # Variabel untuk menyimpan selisih terdekat dari target

    if n > 2:  # Memastikan ada cukup angka untuk diproses
        nums.sort()  # Mengurutkan list angka

        for i in range(
            n - 2
        ):  # Iterasi untuk mencari triplet yang jumlahnya paling mendekati target
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Menghindari triplet yang sama untuk menghindari duplikasi

            j, k = i + 1, n - 1  # Pointer untuk angka kedua dan ketiga dalam triplet

            while j < k:
                _sum = nums[i] + nums[j] + nums[k]  # Menghitung jumlah tiga angka

                if abs(_sum - target) < diff:
                    res = _sum  # Memperbarui hasil terdekat
                    diff = abs(
                        _sum - target
                    )  # Memperbarui selisih terdekat dengan target

                if _sum == target:
                    return res  # Jika jumlah tiga angka sama dengan target, langsung kembalikan hasil
                elif _sum > target:
                    k -= 1  # Jika jumlah terlalu besar, kurangi angka ketiga
                else:
                    j += 1  # Jika jumlah terlalu kecil, tambahkan angka kedua

    return res  # Kembalikan hasil yang jumlahnya paling mendekati target
