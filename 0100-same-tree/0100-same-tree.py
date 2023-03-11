# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        a_list, b_list = list(), list()
        def profile(target_l, depth, tag, p: Optional[TreeNode]):
            if p is None:
                return
            else:
                target_l.append(f'{depth}_{p.val}_{tag}')
                if p.left:
                    profile(target_l, depth+1, 'left', p.left)
                if p.right:
                    profile(target_l, depth+1, 'right', p.right)
        profile(a_list, 0, 'root', p)
        profile(b_list, 0, 'root', q)
        
        if len(a_list) != len(b_list):
            return False
        
        for item in a_list:
            if item not in b_list:
                return False
        
        return True
                
                