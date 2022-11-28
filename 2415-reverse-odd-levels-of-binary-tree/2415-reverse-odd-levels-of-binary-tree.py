# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from queue import Queue
        import math
        Q, depth = Queue(), 0
        Q.put(root)
        
        while Q.qsize():
            temp_list = list()
            for _ in range(Q.qsize()):
                node = Q.get()
                temp_list.append(node)
                if node.left:
                    Q.put(node.left)
                if node.right:
                    Q.put(node.right)
            if depth & 1 == 1:
                digit_list = [x.val for x in temp_list]
                digit_list = digit_list[::-1]
                for node, d in zip(temp_list, digit_list):
                    node.val = d
            else:
                del temp_list
            depth += 1
        return root
        
        