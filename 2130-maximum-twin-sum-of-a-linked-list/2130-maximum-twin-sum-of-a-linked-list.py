# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp, n = head, 0
        ans_list, ans = list(), -10e4
        while temp:
            ans_list.append(temp.val)
            temp = temp.next
        for i in range(len(ans_list) // 2):
            ans = max(ans, ans_list[i] + ans_list[len(ans_list) - 1 - i])
        return ans
            
        