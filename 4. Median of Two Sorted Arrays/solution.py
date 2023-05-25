from typing import List

class Solution:
    def find_median(self, nums):
        arr_len = len(nums)
        if arr_len == 0: 
            return 0
        half = arr_len//2
        if arr_len%2 == 0:
            target_indexes = [half - 1, half]
        else:
            target_indexes = [half]
        l = 0
        s = 0
        for i in target_indexes:
            s += nums[i]
            l += 1
        return s/l

    def join_arrays(self, nums1: List, nums2: List):
        return sorted(nums1 + nums2)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.find_median(self.join_arrays(nums1, nums2))
    