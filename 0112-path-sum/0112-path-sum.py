# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return targetSum == root.val if root and root.left is None and root.right is None else root and (self.hasPathSum(root.right, targetSum - root.val) or self.hasPathSum(root.left, targetSum - root.val)) 