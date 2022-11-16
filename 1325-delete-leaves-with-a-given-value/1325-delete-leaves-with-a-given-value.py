# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        #if root:
        #    print(f'root.val : {root.val}')
        
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        if root.left is None and root.right is None:
            #if root.val == target:
            #    print(f'leave and target')
            return None if root.val == target else root
        
        return root
        