from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the most recent index of each character
        char_index_map = defaultdict(lambda: -1)
        l = 0  # Left pointer of the sliding window
        max_length = 0

        # Iterate through the string using the right pointer
        for r, c in enumerate(s):
            # Move the left pointer right if we have seen the character before
            # and it lies within the current window
            l = max(l, char_index_map[c] + 1)
            
            # Update the last seen index of the character
            char_index_map[c] = r

            # Calculate the current length of the window and update max_length
            max_length = max(max_length, r - l + 1)

        return max_length

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Input: {s}")
    print(f"Length of the longest substring without repeating characters: {result}")
