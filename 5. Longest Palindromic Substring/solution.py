class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindomes = []
        l = len(s)
        for step in range(l):
            for i in range(step+1):
                cur = s[i:l-step+i]
                print(cur)
                if self.isPalyndrome(cur):
                    return cur


    def isPalyndrome(self, s):
        return s == s[::-1]
    
Solution().longestPalindrome("babad")