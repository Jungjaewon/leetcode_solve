# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = [None]
        def func(ans: List, node: TreeNode, target: TreeNode):
            if node is None:
                return
            if node.val == target.val:
                ans[0] = node
                return
            else:
                func(ans, node.left, target)
                func(ans, node.right, target)
        func(ans, cloned, target)
        return ans[0]