# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_list, ans = list(), ListNode()
        temp, temp_v = ans, 0
        #head = head.next 
        while head:
            if head.val == 0:
                if temp_v != 0:
                    ans_list.append(temp_v)
                temp_v = 0
            else:
                temp_v += head.val
            head = head.next
        for i, v in enumerate(ans_list):
            temp.val = v
            if i + 1 != len(ans_list):
                temp.next = ListNode()
            temp = temp.next
            
        return ans
        """
        ans = ListNode()
        temp, temp_v = ans, 0  
        while head:
            if head.val == 0:
                if temp_v != 0:
                    temp.val = temp_v
                    if head.next is not None:
                        temp.next = ListNode()
                    temp = temp.next
                temp_v = 0
            else:
                temp_v += head.val
            head = head.next
        return ans
        """
        