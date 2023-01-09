# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_l, ans, cnt = list(), head, 0
        while head:
            temp_l.append(head.val)
            head = head.next
        temp_l, head = temp_l[::-1], ans
        for i in range(len(temp_l)):
            head.val = temp_l[i]
            head = head.next
        return ans
        
        
        """
        if head is None:
            return None
        temp_l, temp = list(), ListNode()
        ans, cnt = temp, 0
        while head:
            temp_l.append(head.val)
            head = head.next
        temp_l = temp_l[::-1]
        while temp:
            temp.val = temp_l[cnt]
            if cnt + 1 != len(temp_l):
                temp.next = ListNode()
            temp = temp.next
            cnt += 1
        return ans
        """
        
        