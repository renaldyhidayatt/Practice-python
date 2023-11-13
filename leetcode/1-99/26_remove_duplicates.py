def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0  # Mengembalikan 0 jika list kosong

    last, finder = 0, 0

    while last < len(nums) - 1:
        # Memindahkan penanda 'finder' untuk menemukan angka yang berbeda
        while nums[finder] == nums[last]:
            finder += 1

            # Jika 'finder' mencapai akhir list, return panjang list yang sudah dimodifikasi
            if finder == len(nums):
                return last + 1

        # Mengganti nilai di 'last + 1' dengan nilai yang berbeda
        nums[last + 1] = nums[finder]

        last += 1  # Menyesuaikan posisi terakhir setelah mengganti nilai

    return last + 1  # Mengembalikan panjang list yang sudah dimodifikasi
