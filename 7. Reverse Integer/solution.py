class Solution:
    def reverse(self, x: int) -> int:
        k = 1 if x >= 0 else -1
        _x = int(str(abs(x))[::-1])
        if _x >= 2**31 - 1:
            _x = 0
        return _x * k
    
a = Solution().reverse(1534236469)
print(a)