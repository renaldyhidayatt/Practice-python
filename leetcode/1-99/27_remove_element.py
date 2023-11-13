def removeElement(nums, val):
    if len(nums) == 0:
        return 0  # Mengembalikan 0 jika list kosong

    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            if i != j:
                # Jika nilai tidak sama dengan 'val', tukar nilai di 'i' dengan nilai di 'j'
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return j  # Mengembalikan panjang list yang sudah dimodifikasi setelah menghapus nilai 'val'
