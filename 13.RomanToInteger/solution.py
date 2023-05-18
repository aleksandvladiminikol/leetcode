class Solution:
    rules = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int:
        total = 0
        previos = None
        for i in s[::-1]:
            current = self.rules[i]
            if previos and previos > current:
                total -= current
            else:
                total += current
            previos = current
        return total
    
a = Solution()
print(a.romanToInt('MCMXCIV'))