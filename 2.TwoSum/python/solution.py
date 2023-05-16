from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            remaining = target - num
            try:
                index_0 = nums.index(remaining)
            except ValueError:
                continue
            if index_0 == index:
                continue
            return (index, index_0)

