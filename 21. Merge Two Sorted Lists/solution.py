from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        parent_node = ListNode()
        current_node = parent_node
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    current_node.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    current_node.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            current_node = current_node.next

        return parent_node.next


listnode1 = None
listnode2 = ListNode(0)
a = Solution().mergeTwoLists(listnode1, listnode2)