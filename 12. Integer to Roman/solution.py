class Solution:
    def intToRoman(self, num: int) -> str:
        rules = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100:"C",
            500:"D",
            1000:"M"
        }
        res = ""
        for i in range(4):
            _num = num % 10
            if _num == 4:
                res = rules[10**i] + rules[5*10**i] + res
            elif _num == 9:
                res = rules[10**i] + rules[10**(i+1)] + res
            else:
                if _num >= 5:
                    res = rules[5*10**i] + rules[10**i] * (_num - 5) + res
                else:
                    res = rules[10**i] * _num + res
            num //= 10
        return res
                    

                    

# Input: num = 1994
# Output: "MCMXCIV"
print(Solution().intToRoman(1994))