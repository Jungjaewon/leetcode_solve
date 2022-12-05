# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = list()
        def help(root: TreeNode):
            if root is None:
                return
            else:
                ans.append(root.val)
                help(root.left)
                help(root.right)
        help(root1)
        help(root2)
        return sorted(ans)
        