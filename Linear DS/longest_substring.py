from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "babcbdefg"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Input: {s}")
    print(f"Length of the longest substring without repeating characters: {result}")
