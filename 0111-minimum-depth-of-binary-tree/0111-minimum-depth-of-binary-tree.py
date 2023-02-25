# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        ans = [10e4]
        def func(depth:int, root: Optional[TreeNode]):
            if root is None:
                return
            if root.left is None and root.right is None:
                ans[0] = min(ans[0], depth)
                return
            else:
                func(depth + 1, root.left)
                func(depth + 1, root.right)
        func(1, root)
        return ans[0] if ans[0] != 10e4 else 0
        """
        """
        if root is None:
            return 0
        else:
            def func(depth:int,  node: Optional[TreeNode]):
                
                if node is None:
                    return 10e4
                elif node.left is None and node.right is None:
                    return depth
                else:
                    return min(func(depth + 1, node.left), func(depth + 1, node.right))
            return func(1, root)
        """
        from queue import Queue
        Q, ans = Queue(), 10e4
        
        if root is None:
            return 0
        else:
            depth = 1
            Q.put(root)
            while Q.qsize():
                for _ in range(Q.qsize()):
                    node = Q.get()
                    if node.left is None and node.right is None:
                        ans = min(ans, depth)

                    if node.left:
                        Q.put(node.left)
                    if node.right:
                        Q.put(node.right)
                depth += 1
            return ans
                
                
                