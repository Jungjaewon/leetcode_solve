# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt, t_cnt = 0, 0
        temp = head
        while temp:
            temp = temp.next
            cnt += 1
        mid = (cnt // 2) 
        #print(f'cnt : {cnt}, mid : {mid}')
        temp = head
        while temp:
            if mid == t_cnt:
                return temp
            temp = temp.next
            t_cnt += 1 
        return None