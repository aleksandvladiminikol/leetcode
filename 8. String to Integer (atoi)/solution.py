import re

class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = '^([-|\+]?[\d]+)'
        numbers = re.findall(pattern, s.strip())
        number = ''.join(numbers)
        k = -1 if '-' in number else 1
        number = number.replace('-', '').replace('+', '')

        if not number:
            return 0
        result = int(number) * k
        if k > 0:
            result = min(result, 2**31 - 1)
        else:
            result = max(result, -2**31)
        return result


s = "   -42"
a = Solution().myAtoi(s)
print(a)
# s = "  442"
# a = Solution().myAtoi(s)
# print(a)
# s = "4193 with words"
# a = Solution().myAtoi(s)
# print(a)

# s = "4193.1235 with words"
# a = Solution().myAtoi(s)
# print(a)

# s = "-4193.1235 with words"
# a = Solution().myAtoi(s)
# print(a)

# s = "asdasd-4193.1235 with words"
# a = Solution().myAtoi(s)

s = "-91283472332"
s = "+1"
a = Solution().myAtoi(s)


print(a)