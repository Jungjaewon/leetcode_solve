# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def func(node : TreeNode):
            if node is None:
                return ""
            else:
                return func(node.left) + f'_{node.val}_' + func(node.right)
        ans = temp = TreeNode()
        s = func(root)
        split_s = [x for x in s.split('_') if x != '']
        for idx, v in enumerate(split_s):
            temp.val = int(v)
            if idx + 1 != len(split_s):
                temp.right = TreeNode()
                temp = temp.right
        return ans