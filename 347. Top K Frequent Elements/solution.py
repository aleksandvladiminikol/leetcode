from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in Counter(nums).most_common(k)]

a=Solution().topKFrequent([1, 2, 2, 3, 3, 3], 2)
print(a)

