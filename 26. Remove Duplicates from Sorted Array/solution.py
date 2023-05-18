from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(set(nums))
    

print(Solution().removeDuplicates([1,1,2]))