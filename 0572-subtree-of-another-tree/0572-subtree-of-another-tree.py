# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        def tree2str(node : Optional[TreeNode]):
            if node is None:
                return 'N'
            else:
                return tree2str(node.left) + tree2str(node.right) + f'{str(node.val)}'
        def func(node: Optional[TreeNode], sub_str: str):
            if node is None:
                return False
            node_str = tree2str(node)
            if node_str == sub_str:
                return True
            else:
                return func(node.left, sub_str) or func(node.right, sub_str) 
        sub_str = tree2str(subRoot)
        return func(root, sub_str)
        """
        def tree2str(node : Optional[TreeNode]):
            if node is None:
                return 'N'
            else:
                return  f'{str(node.val)}' + tree2str(node.left) + tree2str(node.right)
        def func(node: Optional[TreeNode], sub_str: str):
            if node is None:
                return False
            node_str = tree2str(node)
            if node_str == sub_str:
                return True
            else:
                return func(node.left, sub_str) or func(node.right, sub_str) 
        sub_str = tree2str(subRoot)
        return func(root, sub_str)
        
        
