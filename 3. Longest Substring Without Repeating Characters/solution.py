class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        longest_substring_len = 0

        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1  # shorten left side of sliding window to past the character
            char_map[char] = right

            current_len = right - left + 1
            if current_len > longest_substring_len:
                longest_substring_len = current_len
        return longest_substring_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))