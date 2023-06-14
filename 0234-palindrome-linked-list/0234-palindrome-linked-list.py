# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        a_list = list()
        temp = head
        while temp:
            a_list.append(temp.val)
            temp = temp.next
        num_a = len(a_list)
        if num_a & 1: # odd
            if a_list[:(num_a // 2)] == a_list[(num_a // 2) + 1:][::-1]:
                return True
            else:
                return False
        else: # even
            if a_list[:num_a // 2] == a_list[num_a // 2:][::-1]:
                return True
            else:
                return False
        """
        """
        a_list = list()
        while head:
            a_list.append(head.val)
            head = head.next
        num_a = len(a_list)
        if num_a & 1: # odd
            if a_list[:(num_a // 2)] == a_list[(num_a // 2) + 1:][::-1]:
                return True
            else:
                return False
        else: # even
            if a_list[:num_a // 2] == a_list[num_a // 2:][::-1]:
                return True
            else:
                return False
        """
        a_list = list()
        while head:
            a_list.append(head.val)
            head = head.next
        i, j = 0, len(a_list) - 1
        
        while not i > j:
            if a_list[i] != a_list[j]:
                return False
            i, j = i + 1, j -1
        return True