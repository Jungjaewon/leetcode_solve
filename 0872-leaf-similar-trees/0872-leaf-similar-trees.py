# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_list, root2_list = list(), list()
        def func(node, node_list):
            if node is None:
                return
            elif node.left is None and node.right is None:
                node_list.append(node.val)
                return
            else:
                func(node.left, node_list)
                func(node.right, node_list)
        func(root1, root1_list)
        func(root2, root2_list)
        if len(root2_list) != len(root1_list):
            return False
        return all([ x == y for x,y in zip(root1_list, root2_list)])
                