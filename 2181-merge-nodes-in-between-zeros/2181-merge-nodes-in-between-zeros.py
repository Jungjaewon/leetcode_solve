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
        