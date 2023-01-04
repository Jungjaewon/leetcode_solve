# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, val):
            if node is None:
                return 0
            s = 1 if node.val >= val else 0
            max_v = max(node.val, val)
            
            return s + helper(node.left, max_v) + helper(node.right, max_v)
        return helper(root, root.val)
        # https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/2511509/Python-easy-to-understand-solution
        """
        ans = [0]
        def helper(node:TreeNode, path: List[int]):
            if node is None:
                return
            flag = True
            for val in path:
                if val > node.val:
                    flag = False
            if flag:
                ans[0] += 1
            
            path.append(node.val)
            helper(node.left, path)
            #path.pop()
            #path.append(node.val)
            helper(node.right, path)
            path.pop()
        helper(root, [])
        return ans[0]
        """