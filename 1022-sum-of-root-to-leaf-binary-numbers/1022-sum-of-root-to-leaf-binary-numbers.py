# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        ans_list = list()
        def func(root: Optional[TreeNode], s : str):
            if root is None:
                return
            else:
                s = f'{s}{root.val}'
                if root.left is None and root.right is None:
                    ans_list.append(s)
                else:
                    func(root.left, s)
                    func(root.right, s)
        func(root, "")
        return sum([int(x, 2) for x in ans_list])
        """
        """
        ans_list = list()
        def func(root: Optional[TreeNode], s : str):
            if root is None:
                return
            else:
                s += str(root.val)
                if root.left is None and root.right is None:
                    ans_list.append(s)
                else:
                    func(root.left, s)
                    func(root.right, s)
        func(root, "")
        return sum([int(x, 2) for x in ans_list])
        """
        ans = 0 
        def func(root: Optional[TreeNode], n : int):
            nonlocal ans
            if root is None:
                return
            else:
                n = n << 1 | root.val
                if root.left is None and root.right is None:
                    ans += n
                else:
                    func(root.left, n)
                    func(root.right, n)
        func(root, 0)
        return ans