# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans_l = list()
        
        def helper(root: Optional[TreeNode]):
            if root is None:
                return
            else:
                helper(root.left)
                ans_l.append(root.val)
                helper(root.right)
        helper(root)
        return ans_l
        """
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """
        