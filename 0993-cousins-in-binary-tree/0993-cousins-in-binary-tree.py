# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def get_level(node: Optional[TreeNode], key, level=0, pv=-1):
            if node is None:
                return None
            elif node.val == key:
                return [level, pv]
            else:
                return get_level(node.left, key, level + 1, node.val) or get_level(node.right, key, level + 1, node.val)
        x_ret = get_level(root, x, 0)
        y_ret = get_level(root, y, 0)
        return x_ret[0] == y_ret[0] and x_ret[1] != y_ret[1]
            
            