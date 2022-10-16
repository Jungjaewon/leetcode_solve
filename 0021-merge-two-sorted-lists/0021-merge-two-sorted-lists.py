# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        
        cur = dummy = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.val = list1.val
                list1, cur.next = list1.next, ListNode()
            else:
                cur.val = list2.val
                list2, cur.next = list2.next, ListNode()
            cur = cur.next
        
        if list1:
            cur.val = list1.val
            if list1.next:
                cur.next = list1.next
        if list2:
            cur.val = list2.val
            if list2.next:
                cur.next = list2.next
        
        return dummy
        