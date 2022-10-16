# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result_list = list()
        def solve(root: Optional[TreeNode], val: int):
            if root is None:
                return 0
            else:
                if root.left is None and root.right is None:
                    result_list.append(val + root.val)
                    return
                if root.left:
                    solve(root.left, root.val + val)
                if root.right:
                    solve(root.right, root.val + val)
        solve(root, 0)
            
        return targetSum in result_list