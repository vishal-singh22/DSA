
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last - 1

# Test the function
solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [3, 5, 6]
n = 3

print("Before merging:")
print("nums1:", nums1)
print("nums2:", nums2)

solution.merge(nums1, m, nums2, n)

print("After merging:")
print("nums1:", nums1)
