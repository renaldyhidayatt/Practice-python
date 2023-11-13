from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Mengurutkan list untuk mempermudah pencarian

    result = []  # Inisialisasi list untuk menampung hasil
    length = len(nums)

    for index in range(length - 2):  # Iterasi melalui list hingga dua angka terakhir
        # Penanganan angka duplikat untuk menghindari duplikasi solusi
        if index > 0 and nums[index] == nums[index - 1]:
            continue  # Melompati iterasi jika angka pada index ini sama dengan angka sebelumnya

        start, end = index + 1, length - 1  # Menentukan pointer awal dan akhir

        while start < end:
            total = nums[index] + nums[start] + nums[end]  # Menjumlahkan tiga angka

            if total == 0:  # Jika jumlah tiga angka adalah 0 (sesuai dengan permintaan)
                result.append(
                    [nums[index], nums[start], nums[end]]
                )  # Tiga angka ini dimasukkan ke dalam hasil

                # Penanganan angka duplikat di sekitar angka yang cocok
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1  # Pindah ke angka berikutnya untuk dilakukan pengecekan
                end -= 1  # Pindah ke angka sebelumnya untuk dilakukan pengecekan
            elif total < 0:  # Jika jumlahnya kurang dari 0, pindah ke angka berikutnya
                start += 1
            else:  # Jika jumlahnya lebih dari 0, pindah ke angka sebelumnya
                end -= 1

    return result  # Mengembalikan list yang berisi triplet yang jumlahnya 0
