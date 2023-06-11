# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans_list = list()
        def func(root: Optional[TreeNode], s_l : list):
            nonlocal ans_list
            if root is None:
                return
            else:
                s_l.append(str(root.val))
                if root.left is None and root.right is None:
                    ans_list.append('->'.join(s_l))
                func(root.left, copy.deepcopy(s_l))
                func(root.right, copy.deepcopy(s_l))
        func(root, [])
        return ans_list
                
        