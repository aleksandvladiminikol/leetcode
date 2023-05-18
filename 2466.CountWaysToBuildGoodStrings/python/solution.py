import math
from functools import cache

class Solution:
    MOD = 1_000_000_007
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(length: int) -> int:
            if length > high:
                return 0
            return (
                    int(low <= length) +
                    dp(length + zero) +
                    dp(length + one)
            ) % self.MOD

        return dp(0)
    
def main():
    solution = Solution()
    low = 3
    high = 3
    zero = 1
    one = 1
    print(solution.countGoodStrings(low, high, zero, one), f"expected: 8")

main()

