
"""class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        re_set=set()
        for i in nums:
            if i in re_set:
                return i
            else:
                re_set.add(i)"""


def find_duplicate(arr):
    arr.sort()
    for i in range(0,len(arr)):
        if arr[i] == arr[i+1]:
            return arr[i]

num = [3,1,3,4,2]

print(find_duplicate(num))
        
