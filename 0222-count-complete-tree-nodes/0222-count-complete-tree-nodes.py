# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        ans = [0]
        def func(ans, root):
            if root is None:
                return
            else:
                ans[0] += 1
                func(ans, root.left)
                func(ans, root.right)
        func(ans, root)
        return ans[0]
        """
        from queue import Queue
        q, ans = Queue(), 0
        q.put(root)
        while q.qsize():
            node = q.get()
            if node is not None:
                ans += 1
                q.put(node.left)
                q.put(node.right)
        return ans
        