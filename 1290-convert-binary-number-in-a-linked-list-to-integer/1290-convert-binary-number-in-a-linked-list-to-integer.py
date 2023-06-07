# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        a_list, ans = list(), 0
        while head:
            a_list.append(head.val)
            head = head.next
        for idx, b in enumerate(a_list[::-1]):
            ans = ans | 1 << idx if b == 1 else ans
        return ans
        """
        ans = 0
        while head:
            ans = ans << 1 | head.val
            head = head.next
        return ans
                
        