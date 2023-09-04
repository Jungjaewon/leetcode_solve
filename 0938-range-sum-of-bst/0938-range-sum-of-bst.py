# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        if not root:
            return 0
        elif root and low <= root.val and root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif root and not (low <= root.val and root.val <= high):
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        else:
            return 0
        """
        ans = [0]
        
        def func(root: Optional[TreeNode], low: int, high: int):
            if not root:
                return
            elif root and low <= root.val and root.val <= high:
                ans[0] += root.val
                func(root.left, low, high)
                func(root.right, low, high)
            elif root and not (low <= root.val and root.val <= high):
                func(root.left, low, high)
                func(root.right, low, high)
            else:
                return
        func(root, low, high)
        return ans[0]