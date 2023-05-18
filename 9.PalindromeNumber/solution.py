class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = str(x)
        return numbers == numbers[::-1]