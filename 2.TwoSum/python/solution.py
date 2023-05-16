from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in num_set:
                return [i, nums.index(remaining)]
            num_set.add(num)
        return []