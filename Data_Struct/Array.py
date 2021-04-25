from typing import List

#   Duplicate Zeros


class Solution:
    # xoa so 0
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                i = i + 1
            else:
                arr.insert(i+1, 0)
                i = i + 2
                arr.pop()
    # sap xep mega

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # last index nums1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        temp = nums1.copy()
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i = i + 1
            else:
                nums1[k] = nums2[j]
                j = j + 1
            k = k + 1

        while i < m:
            nums1[k] = temp[i]
            i = i + 1
            k = k + 1
        while j < n:
            nums1[k] = nums2[j]
            j = j + 1
            k = k + 1
    # xoa phan tu trong mang

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            else:
                i = i + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # neu so dau va so tiep theo cung co gia thi cat no o phan dau
            if nums[i] in nums[i+1:]:
                nums.remove(nums[i])
            # tiep tuc duyet
            else:
                i = i + 1

    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j] * 2 and i != j:
                    return True
        return False

    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if (n < 3):
            return False
        i = 1
        while (i < n and arr[i] > arr[i-1]):
            i = i + 1
        if (i == 1 or i == n):
            return False
        while (i < n and arr[i] < arr[i-1]):
            i = i + 1
        return i == n

    def replaceElements(self, arr: List[int]) -> List[int]:
        # maxsofar = arr[-1] # dat max la phan tu cuoi
        # arr[-1] = -1 # index cuoi  bang -1
        # duyet tu cuoi mang den dau mang
        # for i in range(len(arr)-2,-1,-1):
        # maxsofar,arr[i] = max(maxsofar,arr[i]),maxsofar
        n = len(arr)
        # buoc 1
        # duyet tu cuoi den dau mang
        for i in range(n-2, -1, -1):
            # b1.1 bo qua i == n - 1 la ban than a[n-1]
            # ap dung nguoc lai i != n
            if i != n - 1:
                # b2 cong thuoc tim gia tri lon nhat ben phai
                arr[i] = max(arr[i], arr[i+1])
        # b3 dich toan bo gia tri sang ben trai duyet dau den cuoi mang
        for i in range(1, n):
            # gan vao phan tu ngay trươc no
            arr[i-1] = arr[i]
        # gan phan tu cuoi cung a[n-1] = -1
        if (n > 0):
            arr[n-1] = -1
        return arr


for i in range(10, 1, -1):
    print(i)
