# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            def get_h(node:Optional[TreeNode]):
                if node is None:
                    return 0
                else:
                    return max(get_h(node.left), get_h(node.right)) + 1
                
            left_b, right_b = get_h(root.left), get_h(root.right)
            
            if abs(left_b - right_b) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False