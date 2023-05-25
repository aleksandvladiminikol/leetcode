from typing import List
from itertools import combinations
import heapq


class Solution:
    def maxScore(self, nums1, nums2, k):
        total = res = 0
        heap = []
        
        pairs = zip(nums1, nums2)
        
        sorted_pairs = sorted(pairs, key=lambda x: -x[1])
        
        for pair in sorted_pairs:
            num1, num2 = pair  
            heapq.heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total * num2)
        
        return res

        
nums1 = [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344]
nums2 = [345,229,976,2086,567,726,1640,2451,1829,77,1631,306,2032,2497,551,2005,2009,1855,1685,729,2498,2204,588,474,693,30,2051,1126,1293,1378,1693,1995,2188,1284,1414,1618,2005,1005,1890,30,895,155,526,682,2454,278,999,1417,1682,995]
k = 42

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

factorial = lambda x: 1 if x == 0 else x * factorial(x-1)
s = Solution().maxScore(nums1, nums2, k)
print(s)