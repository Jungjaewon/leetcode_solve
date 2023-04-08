# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ans = list()
        def func(root:Optional[TreeNode]):
            if root is None:
                return
            else:
                ans.append(root.val)
                func(root.left)
                func(root.right)
        func(root)
        return len(set(ans)) == 1