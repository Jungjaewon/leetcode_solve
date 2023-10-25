# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def func(node):
            if node is None:
                return []
            else:
                return [node.val] + func(node.left) + func(node.right)
        ret = func(root)
        if len(ret):
            ret = sorted(ret)
            m_v = min(ret)
            for n in ret:
                if n != m_v:
                    return n
        return -1