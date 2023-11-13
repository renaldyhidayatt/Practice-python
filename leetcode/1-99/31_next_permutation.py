def nextPermutation(nums: list[int]):
    i, j = 0, 0

    # Mencari indeks pertama dari belakang yang melanggar pola monotonik menurun
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break

    # Jika ada pola monotonik yang dilanggar
    if i >= 0:
        # Mencari bilangan pertama yang lebih besar dari bilangan pada indeks i
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                break

        # Menukar bilangan pada indeks i dengan bilangan pertama yang lebih besar dari belakang
        nums[i], nums[j] = nums[j], nums[i]

    # Melakukan pembalikan urutan bilangan setelah indeks i untuk mendapatkan permutasi selanjutnya
    reverse(nums, i + 1, len(nums) - 1)


def reverse(nums, i, j):
    # Fungsi untuk membalik urutan bilangan dari indeks i hingga j
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
