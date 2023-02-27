# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        if root is None:
            return False
        def helper(node : Optional[TreeNode]) -> bool:
            if node.left is None and node.right is None:
                return node.val
            else:
                if node.val == 2:
                    return helper(node.left) | helper(node.right)
                else:
                    return helper(node.left) & helper(node.right)
        return helper(root)
        """
        
        if root is None:
            return False
        else:
            if root.left is None and root.right is None:
                return root.val
            if root.val == 2:
                return self.evaluateTree(root.left) | self.evaluateTree(root.right)
            else:
                return self.evaluateTree(root.left) & self.evaluateTree(root.right)
            
        
        
                
        