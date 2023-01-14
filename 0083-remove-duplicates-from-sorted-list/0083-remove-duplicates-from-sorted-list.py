# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans_set, ans = set(), ListNode()
        temp = ans
        while head:
            ans_set.add(head.val)
            head = head.next
        ans_list = sorted(list(ans_set))
        for i, n in enumerate(ans_list):
            temp.val = n
            if i + 1 != len(ans_list):
                temp.next = ListNode()
                temp = temp.next
        return ans
            
        