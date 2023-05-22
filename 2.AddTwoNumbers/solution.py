from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def read_number(self, l: Optional[ListNode]) -> str:
        if l.next is None:
            return str(l.val)
        else:
            return str(l.val) + self.read_number(l.next)
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = int(self.read_number(l1)[::-1])
        num2 = int(self.read_number(l2)[::-1])
        sum = num1 + num2
        sum_str = str(sum)
        sum_node = None
        for i in sum_str:
            sum_node = ListNode(int(i), sum_node)
        return sum_node

Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))