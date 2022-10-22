# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        
        def func(root: Optional[TreeNode], type_n, ans):
            
            if root is None:
                return
            elif type_n == 'left' and root.left is None and root.right is None:
                ans[0] += root.val
                
            func(root.left, "left", ans)
            func(root.right, "right", ans)
        
        func(root, "root", ans)
        return ans[0]
            
            
            
        