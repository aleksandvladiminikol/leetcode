from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)
        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            if self.nums[0] < val:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
        return self.nums[0]

#case = [[2,[0]],[-1],[1],[-2],[-4],[3]]
kthLargest = KthLargest(2, [0])
a1 = kthLargest.add(-1);   #// return 4
a2 = kthLargest.add(1);   #// return 5
a3 = kthLargest.add(-2);  #// return 5
a4 = kthLargest.add(-4);   #// return 8
a5 = kthLargest.add(3);   #// return 8
print(a1, a2, a3, a4, a5)


# case = [[1,[]],[-3],[-2],[-4],[0],[4]]
kthLargest = KthLargest(1, [])
a1 = kthLargest.add(-3);   #// return 4
a2 = kthLargest.add(-2);   #// return 5
a3 = kthLargest.add(-4);  #// return 5
a4 = kthLargest.add(0);   #// return 8
a5 = kthLargest.add(4);   #// return 8
print(a1, a2, a3, a4, a5)



kthLargest = KthLargest(3, [4, 5, 8, 2])



a1 = kthLargest.add(3);   #// return 4
a2 = kthLargest.add(5);   #// return 5
a3 = kthLargest.add(10);  #// return 5
a4 = kthLargest.add(9);   #// return 8
a5 = kthLargest.add(4);   #// return 8

print(a1, a2, a3, a4, a5)