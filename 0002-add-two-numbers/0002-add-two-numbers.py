# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, carry = ListNode(), 0
        ret = ans
        
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = l1_val + l2_val
            
            result = ((sum_val % 10) + carry) % 10
            carry = (sum_val + carry) // 10
            
            ans.next = ListNode(val= result)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None    
            ans = ans.next
            
        if carry > 0:
            ans.next = ListNode()
            ans = ans.next
            ans.val = carry            
        return ret.next
        
        """
        a_list, b_list = list(), list()
        while l1:
            a_list.append(str(l1.val))
            l1 = l1.next
        while l2:
            b_list.append(str(l2.val))
            l2 = l2.next
        a_int, b_int = int(''.join(a_list[::-1])), int(''.join(b_list[::-1]))
        temp = ListNode()
        ans = temp
        result_str = str(a_int + b_int)[::-1]
        for idx, c in enumerate(result_str):
            temp.val = int(c)
            if len(result_str) == idx + 1:
                break
                
            temp.next = ListNode()
            temp = temp.next
        return ans
        """
        
        
        