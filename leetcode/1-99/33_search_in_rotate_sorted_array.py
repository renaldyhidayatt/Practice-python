from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1  # Kondisi untuk pengecekan jika array kosong

    low, high = (
        0,
        len(nums) - 1,
    )  # Penetapan indeks awal dan akhir dalam pencarian biner

    while low <= high:
        mid = low + (high - low) // 2  # Temukan titik tengah untuk pencarian biner

        if nums[mid] == target:
            return mid  # Return indeks jika target ditemukan di tengah array

        elif nums[mid] > nums[low]:  # Jika bagian kiri terurut secara normal
            if nums[low] <= target < nums[mid]:
                high = mid - 1  # Update batas atas jika target ada di bagian kiri
            else:
                low = mid + 1  # Update batas bawah jika target ada di bagian kanan

        elif nums[mid] < nums[high]:  # Jika bagian kanan terurut secara normal
            if nums[mid] < target <= nums[high]:
                low = mid + 1  # Update batas bawah jika target ada di bagian kanan
            else:
                high = mid - 1  # Update batas atas jika target ada di bagian kiri

        else:  # Penanganan ketika terdapat duplikasi di array
            if nums[low] == nums[mid]:
                low += 1  # Pindahkan batas bawah jika elemen di kiri sama dengan elemen tengah
            if nums[high] == nums[mid]:
                high -= 1  # Pindahkan batas atas jika elemen di kanan sama dengan elemen tengah

    return -1  # Return -1 jika target tidak ditemukan dalam array
