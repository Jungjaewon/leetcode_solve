# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(depth : int, root : Optional[TreeNode]) -> int:
            if root is None:
                return depth
            else:
                #print(f'depth : {depth}, root.val : {root.val}')
                return max(helper(depth + 1, root.left), helper(depth + 1, root.right))
        return helper(0, root)