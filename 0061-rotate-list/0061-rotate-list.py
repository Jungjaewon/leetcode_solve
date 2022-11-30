# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        from collections import deque
        deq, cnt = deque(), 0
        temp = head
        
        while temp:
            deq.append(temp.val)
            temp = temp.next
            cnt += 1
        k = k % cnt if cnt > 0 else k
        temp = head
        deq.rotate(k)
        
        while cnt > 0 :
            a = deq.popleft()
            temp.val = a
            temp = temp.next
            cnt -= 1
        
        return head