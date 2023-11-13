from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()  # Mengurutkan list angka untuk mempermudah pencarian
    n = len(nums)
    quadruplets = (
        []
    )  # List untuk menampung semua kombinasi angka yang sesuai dengan target

    for i in range(n - 3):
        # Penanganan angka duplikat dan pengecekan jumlah minimal dengan angka terbesar
        if i > 0 and (
            nums[i] == nums[i - 1]
            or nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target
        ):
            continue  # Melanjutkan iterasi jika angka pada index ini sama dengan angka sebelumnya

        for j in range(i + 1, n - 2):
            # Penanganan angka duplikat dan pengecekan jumlah minimal dengan angka terbesar
            if j > i + 1 and (
                nums[j] == nums[j - 1]
                or nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target
            ):
                continue  # Melanjutkan iterasi jika angka pada index ini sama dengan angka sebelumnya

            left, right = j + 1, n - 1  # Pointer untuk angka ketiga dan keempat

            while left < right:
                total = (
                    nums[i] + nums[j] + nums[left] + nums[right]
                )  # Menghitung total empat angka

                if total == target:  # Jika total sesuai dengan target
                    quadruplets.append(
                        [nums[i], nums[j], nums[left], nums[right]]
                    )  # Tambahkan ke dalam hasil

                    left += 1
                    right -= 1

                    # Penanganan angka duplikat di sekitar angka yang cocok
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:  # Jika total terlalu kecil
                    left += 1  # Naikkan angka ketiga
                else:  # Jika total terlalu besar
                    right -= 1  # Turunkan angka keempat

    return quadruplets  # Kembalikan semua kombinasi angka yang jumlahnya sama dengan target
