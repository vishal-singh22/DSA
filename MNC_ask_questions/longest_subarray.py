"""Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.
"""


def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) 

    left, right = 0, 0 
    Sum = a[0]
    maxLen = 0
    while right < n:
    
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1


        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        right += 1
        if right < n: Sum += a[right]

    return maxLen


if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")
