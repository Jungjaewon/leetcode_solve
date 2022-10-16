# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def solve(root: Optional[TreeNode], currSum: int, targetSum: int):
            
            if root is None:
                return False
            
            currSum += root.val
            
            if root.left is None and root.right is None:
                return currSum == targetSum
            return solve(root.left, currSum, targetSum) or solve(root.right, currSum, targetSum)
            
        
        if root is None:
            return False
        else:
            return solve(root, 0, targetSum)