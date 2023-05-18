from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_prefix = ''
        index = 0
        while True:
            try:
                current = strs[0][index]
            except IndexError:
                return max_prefix
            for i in strs:
                try:
                    if i[index] != current:
                        return max_prefix
                except IndexError:
                    return max_prefix
            max_prefix += current
            index += 1

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
