# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans, a_head = list(), ListNode()
        temp = a_head
        while head:
            ans.append(head.val)
            head = head.next
        ans.sort()
        for idx, i in enumerate(ans):
            a_head.val = i
            if idx + 1 != len(ans):
                a_head.next = ListNode()
                a_head = a_head.next
        return temp if len(ans) > 0 else None
            
        