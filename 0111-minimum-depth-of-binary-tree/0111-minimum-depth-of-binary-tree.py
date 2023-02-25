# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = [10e4]
        def func(depth:int, root: Optional[TreeNode]):
            if root is None:
                return
            if root.left is None and root.right is None:
                ans[0] = min(ans[0], depth)
                return
            else:
                func(depth + 1, root.left)
                func(depth + 1, root.right)
        func(1, root)
        return ans[0] if ans[0] != 10e4 else 0