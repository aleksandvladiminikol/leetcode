from solution import Solution

def main():
    solution = Solution()
    low = 10
    high = 10
    zero = 2
    one = 1
    print(solution.countGoodStrings(low, high, zero, one), f"expected: 89")

main()